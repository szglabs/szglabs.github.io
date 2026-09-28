import re
import json

cities_data = [
    {
        "filename": "phoenix-it-consulting.html",
        "city_name": "Phoenix",
        "short_city": "Phoenix",
        "region": "Phoenix and the Valley of the Sun",
        "area_served": '[\n        "Phoenix",\n        "Scottsdale",\n        "Tempe",\n        "Mesa",\n        "Chandler",\n        "Gilbert"\n      ]',
        "ind_1_title": "Manufacturing & Supply Chain",
        "ind_1_desc": "We design complex integration layers and secure data pipelines that sync suppliers, shop floor operations, and ERP systems (like Odoo) to optimize production and ensure compliance.",
        "ind_2_title": "Healthcare Tech & E-Commerce",
        "ind_2_desc": "We connect point-of-sale, inventory, and enterprise resource planning systems to create unified experiences for growing Arizona brands.",
        "market_desc": "Phoenix is one of the fastest-growing business markets in the country"
    },
    {
        "filename": "salt-lake-city-it-consulting.html",
        "city_name": "Salt Lake City",
        "short_city": "SLC",
        "region": "Salt Lake City and the Silicon Slopes",
        "area_served": '[\n        "Salt Lake City",\n        "Lehi",\n        "Provo",\n        "Orem",\n        "Sandy",\n        "West Valley City"\n      ]',
        "ind_1_title": "SaaS & Technology Platforms",
        "ind_1_desc": "From high-availability cloud infrastructure to custom product features, we build scalable backends and APIs that help growing software companies accelerate their roadmaps.",
        "ind_2_title": "E-Commerce & Retail",
        "ind_2_desc": "We connect point-of-sale, warehouse management, and enterprise resource planning systems to create unified omnichannel experiences for growing Utah brands.",
        "market_desc": "Salt Lake City is a booming tech hub"
    },
    {
        "filename": "san-francisco-it-consulting.html",
        "city_name": "San Francisco",
        "short_city": "SF",
        "region": "San Francisco and the Bay Area",
        "area_served": '[\n        "San Francisco",\n        "San Jose",\n        "Palo Alto",\n        "Mountain View",\n        "Oakland",\n        "Santa Clara"\n      ]',
        "ind_1_title": "Technology Startups & Enterprises",
        "ind_1_desc": "We provide Silicon Valley-caliber senior engineering without the bloated agency overhead, accelerating AI/LLM integrations and complex cloud architectures.",
        "ind_2_title": "SaaS & Financial Tech",
        "ind_2_desc": "From high-volume transaction processing to secure cloud infrastructure, we build backends and data pipelines that meet strict compliance and scaling demands.",
        "market_desc": "San Francisco is the epicenter of global technology"
    },
    {
        "filename": "austin-it-consulting.html",
        "city_name": "Austin",
        "short_city": "Austin",
        "region": "Austin and Central Texas",
        "area_served": '[\n        "Austin",\n        "Round Rock",\n        "Cedar Park",\n        "Georgetown",\n        "Pflugerville",\n        "San Marcos"\n      ]',
        "ind_1_title": "Enterprise Software & Tech Infrastructure",
        "ind_1_desc": "We architect and deploy secure AI applications, intelligent automation, and scalable cloud environments for Austin's rapidly growing tech sector.",
        "ind_2_title": "Logistics & E-Commerce",
        "ind_2_desc": "We connect point-of-sale, warehouse management, and enterprise resource planning systems to create unified omnichannel experiences for growing Texas brands.",
        "market_desc": "Austin is experiencing massive tech migration and growth"
    },
    {
        "filename": "dallas-it-consulting.html",
        "city_name": "Dallas",
        "short_city": "DFW",
        "region": "Dallas-Fort Worth",
        "area_served": '[\n        "Dallas",\n        "Fort Worth",\n        "Arlington",\n        "Plano",\n        "Irving",\n        "Frisco"\n      ]',
        "ind_1_title": "Corporate Enterprise & ERP",
        "ind_1_desc": "We specialize in Odoo ERP implementation and complex EDI integrations (850, 856, 810) that sync operations for large-scale corporate headquarters.",
        "ind_2_title": "Logistics & Supply Chain",
        "ind_2_desc": "We design complex integration layers and secure data pipelines that sync suppliers, warehouses, and ERP systems to optimize massive logistics networks.",
        "market_desc": "Dallas is one of the largest corporate headquarters hubs in the U.S."
    }
]

with open('/root/projects/agy/szg/las-vegas-it-consulting.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

for city in cities_data:
    content = base_content
    
    # Meta / Title
    content = content.replace('Las Vegas IT & AI Consulting | SZG Labs', f"{city['city_name']} IT & AI Consulting | SZG Labs")
    content = content.replace('Local senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for {city['city_name']} businesses.")
    content = content.replace('Las Vegas IT consulting, Las Vegas AI consulting, systems integration Las Vegas, ERP implementation, cloud architecture, hospitality technology, AWS, LLM integration Nevada', f"{city['city_name']} IT consulting, {city['city_name']} AI consulting, systems integration {city['short_city']}, ERP implementation, cloud architecture, tech consulting, AWS, LLM integration")
    
    content = content.replace('Las Vegas IT & AI Consulting | Senior Systems Integration | SZG Labs', f"{city['city_name']} IT & AI Consulting | Senior Systems Integration | SZG Labs")
    content = content.replace('Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for {city['city_name']} businesses.")
    
    content = content.replace('las-vegas-it-consulting.html', city['filename'])
    
    # JSON-LD
    content = content.replace('SZG Labs - Las Vegas IT & AI Consulting', f"SZG Labs - {city['city_name']} IT & AI Consulting")
    
    old_area = r'"areaServed": \[\s*"Las Vegas",\s*"Henderson",\s*"Summerlin",\s*"North Las Vegas",\s*"Paradise",\s*"Spring Valley"\s*\]'
    content = re.sub(old_area, f'"areaServed": {city["area_served"]}', content)
    
    # Remove geo tags from template if present
    content = re.sub(r'<meta name="geo\.region".*?>\n?', '', content)
    content = re.sub(r'<meta name="geo\.placename".*?>\n?', '', content)
    content = re.sub(r'<meta name="geo\.position".*?>\n?', '', content)
    content = re.sub(r'<meta name="ICBM".*?>\n?', '', content)
    content = re.sub(r'"geo":\s*{\s*"@type":\s*"GeoCoordinates",\s*"latitude":\s*36\.1601,\s*"longitude":\s*-115\.1465\s*},', '', content)
    
    # Body replacements
    content = content.replace('IT & AI Consulting for Las Vegas Businesses', f"IT & AI Consulting for {city['city_name']} Businesses")
    content = content.replace('across the Las Vegas metro', f"across the {city['city_name']} metro")
    
    content = content.replace('The Las Vegas Advantage', f"The SZG Labs Advantage in {city['city_name']}")
    content = content.replace('Las Vegas is one of the fastest-growing business markets in the country', city['market_desc'])
    content = content.replace('SZG Labs was founded in Las Vegas to fill that gap.', 'SZG Labs brings senior engineering expertise to fill the gaps left by traditional agencies.')
    content = content.replace('alt="Las Vegas skyline at night"', f'alt="{city["city_name"]}"')
    content = content.replace('Based in Las Vegas and available for on-site engagements across the metro area.', f"Based in Las Vegas, we provide on-site engagements across {city['region']} when needed.")
    
    content = content.replace('Las Vegas industries we know', f"{city['city_name']} industries we know")
    content = content.replace('growing Las Vegas companies', f"growing {city['short_city']} companies")
    
    content = content.replace('Built for Las Vegas operators', f"Built for {city['city_name']} operators")
    content = content.replace('across Las Vegas, Henderson, Summerlin, and the resort corridor.', f"across {city['region']}.")
    
    # Industries
    content = content.replace('<h3>Hospitality & Gaming</h3>', f"<h3>{city['ind_1_title']}</h3>")
    content = content.replace('<p>From high-volume transaction processing to guest experience personalization, we build secure systems that integrate with property management systems (PMS) and gaming platforms.</p>', f"<p>{city['ind_1_desc']}</p>")
    
    content = content.replace('<h3>Retail & E-Commerce</h3>', f"<h3>{city['ind_2_title']}</h3>")
    content = content.replace('<p>We connect point-of-sale (POS), warehouse management (WMS), and enterprise resource planning (ERP) systems to create unified omnichannel experiences for local and national retailers.</p>', f"<p>{city['ind_2_desc']}</p>")
    
    # Logistics section is 3rd, keep it generic if needed or just leave as is.
    
    # FAQ Updates
    content = content.replace('Do you provide on-site IT and AI consulting in Las Vegas?', f"Do you provide on-site IT and AI consulting in {city['city_name']}?")
    content = content.replace('Yes. SZG Labs is locally based in downtown Las Vegas and provides on-site technical consulting, architecture planning, and engineering execution across the entire Las Vegas valley, including Henderson, Summerlin, and the resort corridor.', f"SZG Labs is headquartered in Las Vegas, just a short flight away. We provide dedicated, on-site technical consulting, architecture planning, and engineering execution for our {city['city_name']} clients when physical presence is required, seamlessly blending remote engineering with strategic on-site collaboration.")
    
    content = content.replace('How does SZG Labs differ from typical Las Vegas managed IT services (MSPs)?', f"How does SZG Labs differ from typical {city['city_name']} managed IT services (MSPs)?")
    content = content.replace('What AI integration solutions do you provide for Las Vegas businesses?', f"What AI integration solutions do you provide for {city['city_name']} businesses?")
    
    content = content.replace('How do we get started with SZG Labs in Las Vegas?', f"How do we get started with SZG Labs in {city['city_name']}?")
    content = content.replace('contact our Las Vegas office at', 'contact our engineering team at')
    
    content = content.replace('Questions about our Las Vegas IT', f"Questions about our {city['city_name']} IT")
    content = content.replace('Know a Las Vegas operator', f"Know a {city['city_name']} operator")
    content = content.replace('Las Vegas, NV 89101', 'Las Vegas, NV 89101') # Keep HQ address
    
    with open(f"/root/projects/agy/szg/{city['filename']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 5 new city pages.")
