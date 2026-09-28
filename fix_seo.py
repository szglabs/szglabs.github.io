import re

def update_file(filepath, is_vegas):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Meta descriptions
    if is_vegas:
        content = re.sub(
            r'<meta name="description" content="Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas hospitality, retail, logistics, and growth businesses.">',
            r'<meta name="description" content="Local senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.">',
            content
        )
        # 2. Vegas title
        content = re.sub(
            r'<title>Las Vegas IT & AI Consulting \| Senior Systems Integration & Cloud \| SZG Labs</title>',
            r'<title>Las Vegas IT & AI Consulting | SZG Labs</title>',
            content
        )
        # 4. Geo tags
        if '<meta name="geo.region"' not in content:
            geo_tags = """  <meta name="geo.region" content="US-NV">
  <meta name="geo.placename" content="Las Vegas, Nevada">
  <meta name="geo.position" content="36.1601;-115.1465">
  <meta name="ICBM" content="36.1601, -115.1465">
"""
            content = content.replace('<meta name="description"', geo_tags + '  <meta name="description"')
            
        # 5. AI terms (Vegas page)
        content = content.replace(
            "We build private Retrieval-Augmented Generation (RAG) search",
            "We build private Retrieval-Augmented Generation (RAG) search using machine learning and artificial intelligence"
        )
    else:
        # index.html description
        content = re.sub(
            r'<meta name="description" content="SZG Labs delivers senior engineering services in AI systems integration, DevOps, custom software development, data pipelines, and enterprise automation solutions.">',
            r'<meta name="description" content="SZG Labs delivers senior engineering services in AI systems integration, DevOps, custom software development, data pipelines, and enterprise automation.">',
            content
        )
        # 5. AI terms (Index page)
        content = content.replace(
            "SZG Labs provides senior-level engineering services across AI systems & LLM integration",
            "SZG Labs provides senior-level engineering services across artificial intelligence (AI) systems, machine learning, LLM integration"
        )

    # 3. Lazy loading images (below fold)
    # Exclude hero, logo, about which are likely above fold or early
    def replace_img(m):
        img_tag = m.group(0)
        if 'loading="lazy"' in img_tag:
            return img_tag
        if 'hero-img.png' in img_tag or 'logo.svg' in img_tag:
            return img_tag
        return img_tag.replace('<img ', '<img loading="lazy" ')

    content = re.sub(r'<img [^>]+>', replace_img, content)

    # 6. Sitemap link
    if '<link rel="sitemap"' not in content:
        sitemap_link = '  <link rel="sitemap" type="application/xml" href="/sitemap.xml">\n'
        content = content.replace('  <link href="assets/img/favicon.svg"', sitemap_link + '  <link href="assets/img/favicon.svg"')

    with open(filepath, 'w') as f:
        f.write(content)

update_file('/root/projects/agy/szg/index.html', False)
update_file('/root/projects/agy/szg/las-vegas-it-consulting.html', True)

# 7. Robots.txt
with open('/root/projects/agy/szg/robots.txt', 'w') as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://szglabs.com/sitemap.xml\n")

print("Done")
