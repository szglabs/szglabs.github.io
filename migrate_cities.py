import os
import glob
from bs4 import BeautifulSoup
import re

TEMPLATE_FILE = 'index.html'

with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template_html = f.read()

city_pages = glob.glob('*-it-consulting.html')

for page in city_pages:
    print(f"Processing {page}...")
    with open(page, 'r', encoding='utf-8') as f:
        old_soup = BeautifulSoup(f.read(), 'html.parser')

    new_soup = BeautifulSoup(template_html, 'html.parser')

    # 1. Update <head> metadata
    for tag in new_soup.head.find_all(['title', 'meta', 'link']):
        if tag.name == 'title':
            tag.extract()
        elif tag.name == 'meta' and tag.get('name') in ['description', 'keywords', 'geo.region', 'geo.placename', 'geo.position', 'ICBM', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
            tag.extract()
        elif tag.name == 'meta' and tag.get('property') and tag.get('property').startswith('og:'):
            tag.extract()
        elif tag.name == 'link' and tag.get('rel') == ['canonical']:
            tag.extract()

    title_tag = old_soup.find('title')
    seo_tags = []
    if title_tag: seo_tags.append(title_tag)
    
    for meta in old_soup.find_all('meta'):
        name = meta.get('name')
        prop = meta.get('property')
        if name in ['description', 'keywords', 'geo.region', 'geo.placename', 'geo.position', 'ICBM'] or (name and name.startswith('twitter:')):
            seo_tags.append(meta)
        if prop and prop.startswith('og:'):
            seo_tags.append(meta)
            
    canonical_link = old_soup.find('link', rel='canonical')
    if canonical_link: seo_tags.append(canonical_link)
        
    for existing_ld in new_soup.find_all('script', type='application/ld+json'):
        existing_ld.extract()
    ld_json = old_soup.find('script', type='application/ld+json')
    if ld_json: seo_tags.append(ld_json)

    for tag in seo_tags:
        new_soup.head.append(tag)
        new_soup.head.append("\n  ")

    # 2. Extract localized hero content
    old_hero = old_soup.find('section', id='hero')
    if old_hero:
        h1 = old_hero.find('h1')
        p = old_hero.find('p')
        if h1 and p:
            h1_text = h1.get_text(strip=True)
            # Try to split on "for" to keep the nice gradient style
            if " for " in h1_text:
                parts = h1_text.split(" for ", 1)
                part1 = parts[0] + " for "
                part2 = parts[1]
            else:
                part1 = h1_text
                part2 = ""

            new_hero_h1 = new_soup.find('h1', class_='v2-hero-title')
            if new_hero_h1:
                new_hero_h1.clear()
                span1 = new_soup.new_tag('span', attrs={'class': 'gradient-text'})
                span1.string = part1
                new_hero_h1.append(span1)
                if part2:
                    new_hero_h1.append(new_soup.new_tag('br'))
                    span2 = new_soup.new_tag('span', attrs={'class': 'gradient-accent'})
                    span2.string = part2
                    new_hero_h1.append(span2)

            new_hero_p = new_soup.find('p', class_='v2-hero-subtitle')
            if new_hero_p:
                new_hero_p.string = p.get_text(strip=True)

    # 3. Extract localized advantage
    old_advantage = old_soup.find('section', id='advantage')
    if old_advantage:
        content_div = old_advantage.find('div', class_='content')
        if content_div:
            h3 = content_div.find('h3')
            h2 = content_div.find('h2')
            paragraphs = content_div.find_all('p')
            
            adv_title = h3.get_text(strip=True) if h3 else "The Local Advantage"
            adv_subtitle = h2.get_text(strip=True) if h2 else "A Technical Partner Built for This Market"
            
            p_tags_html = ""
            for p_tag in paragraphs:
                p_tags_html += f'<p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 1rem;">{p_tag.get_text(strip=True)}</p>\n'
                
            advantage_html = f"""
  <section id="local-advantage" class="v2-section" style="padding-top: 2rem; padding-bottom: 2rem;">
    <div class="v2-container">
      <div class="v2-content-card" style="padding: 2.5rem; text-align: left;">
         <h3 style="color: var(--accent-cyan); font-family: var(--font-mono); font-size: 0.9rem; text-transform: uppercase; margin-bottom: 1rem;">{adv_title}</h3>
         <h2 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.8rem;">{adv_subtitle}</h2>
         {p_tags_html}
      </div>
    </div>
  </section>
"""
            v2_hero = new_soup.find('section', class_='v2-hero')
            if v2_hero:
                adv_soup = BeautifulSoup(advantage_html, 'html.parser')
                v2_hero.insert_after(adv_soup)

    # 4. Extract localized FAQs
    old_faq = old_soup.find('section', id='faq')
    if old_faq:
        faq_items = old_faq.find_all('div', class_='faq-item')
        if faq_items:
            new_faq_section = new_soup.find('section', id='faq')
            if new_faq_section:
                faq_container = new_faq_section.find('div', style=lambda s: s and 'max-width: 800px' in s)
                if faq_container:
                    faq_container.clear()
                    for item in faq_items:
                        item_h3 = item.find('h3')
                        item_p = item.find('div', class_='faq-content').find('p')
                        if item_h3 and item_p:
                            span_num = item_h3.find('span', class_='num')
                            if span_num: span_num.extract()
                            q_text = item_h3.get_text(strip=True)
                            a_text = item_p.get_text(strip=True)
                            
                            new_faq_item_html = f"""
        <div class="schematic-node" style="padding: 1.5rem; margin-bottom: 1rem;">
          <h4 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: #fff;">{q_text}</h4>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">{a_text}</p>
        </div>
"""
                            faq_container.append(BeautifulSoup(new_faq_item_html, 'html.parser'))

    with open(page, 'w', encoding='utf-8') as f:
        f.write(str(new_soup))
    
    print(f"Successfully updated {page}")

