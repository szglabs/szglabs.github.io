import re
import json

cities_data = [
    {
        "filename": "new-york-it-consulting.html",
        "city_name": "New York City",
        "short_city": "NYC",
        "region": "New York and the Tri-State Area",
        "area_served": '[\n        "New York",\n        "Manhattan",\n        "Brooklyn",\n        "Queens",\n        "Jersey City",\n        "Hoboken"\n      ]',
        "ind_1_title": "Financial Tech & Media",
        "ind_1_desc": "We build high-frequency data pipelines, secure cloud architectures, and LLM integrations for some of the most demanding compliance and transaction environments in the world.",
        "ind_2_title": "Global Retail & E-Commerce",
        "ind_2_desc": "We connect point-of-sale, inventory, and enterprise resource planning systems to create unified omnichannel experiences for national brands headquartered in NYC.",
        "market_desc": "New York City is the world's most demanding corporate market"
    },
    {
        "filename": "boston-it-consulting.html",
        "city_name": "Boston",
        "short_city": "Boston",
        "region": "Boston and the Greater New England Area",
        "area_served": '[\n        "Boston",\n        "Cambridge",\n        "Somerville",\n        "Waltham",\n        "Newton",\n        "Brookline"\n      ]',
        "ind_1_title": "Healthcare Tech & Biotech",
        "ind_1_desc": "We design highly secure, HIPAA-compliant data pipelines and AI integration layers that allow healthcare organizations to scale operations safely.",
        "ind_2_title": "Enterprise SaaS Platforms",
        "ind_2_desc": "From high-availability cloud infrastructure to custom product features, we build scalable backends and APIs that help growing software companies accelerate their roadmaps.",
        "market_desc": "Boston is a hub of deep tech and medical innovation"
    },
    {
        "filename": "washington-dc-it-consulting.html",
        "city_name": "Washington, D.C.",
        "short_city": "D.C.",
        "region": "Washington D.C., Maryland, and Northern Virginia",
        "area_served": '[\n        "Washington D.C.",\n        "Arlington",\n        "Alexandria",\n        "Bethesda",\n        "Reston",\n        "Tysons"\n      ]',
        "ind_1_title": "Government Contractors & Cybersecurity",
        "ind_1_desc": "We provide senior-level DevOps engineering, infrastructure-as-code (IaC), and secure cloud architecture for mission-critical operations in the DMV area.",
        "ind_2_title": "Telecom & Cloud Infrastructure",
        "ind_2_desc": "Located near the heart of AWS US-East, we build high-throughput data pipelines and event-driven architectures for massive-scale enterprises.",
        "market_desc": "The D.C. metro area requires mission-critical reliability"
    },
    {
        "filename": "atlanta-it-consulting.html",
        "city_name": "Atlanta",
        "short_city": "Atlanta",
        "region": "Atlanta and the Southeast",
        "area_served": '[\n        "Atlanta",\n        "Alpharetta",\n        "Marietta",\n        "Roswell",\n        "Sandy Springs",\n        "Decatur"\n      ]',
        "ind_1_title": "Logistics & Supply Chain",
        "ind_1_desc": "We design complex integration layers and secure data pipelines that sync suppliers, global shipping operations, and ERP systems to optimize massive supply networks.",
        "ind_2_title": "Corporate Enterprise & ERP",
        "ind_2_desc": "We specialize in Odoo ERP implementation and complex EDI integrations (850, 856, 810) that sync operations for large-scale corporate headquarters.",
        "market_desc": "Atlanta is a global powerhouse for logistics and corporate headquarters"
    },
    {
        "filename": "miami-it-consulting.html",
        "city_name": "Miami",
        "short_city": "Miami",
        "region": "Miami and South Florida",
        "area_served": '[\n        "Miami",\n        "Fort Lauderdale",\n        "Coral Gables",\n        "Miami Beach",\n        "Boca Raton",\n        "West Palm Beach"\n      ]',
        "ind_1_title": "FinTech & Startups",
        "ind_1_desc": "We architect and deploy secure AI applications, intelligent automation, and scalable cloud environments for South Florida's rapidly growing tech sector.",
        "ind_2_title": "E-Commerce & LATAM Gateway",
        "ind_2_desc": "We connect point-of-sale, warehouse management, and enterprise resource planning systems to create unified operational backbones for international commerce.",
        "market_desc": "Miami is experiencing explosive growth in tech and finance"
    }
]

with open('/root/projects/agy/szg/las-vegas-it-consulting.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

for city in cities_data:
    content = base_content
    
    # Meta / Title
    content = content.replace('Las Vegas IT & AI Consulting | SZG Labs', f"{city['city_name']} IT & AI Consulting | SZG Labs")
    content = content.replace('Local senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"National senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for {city['city_name']} businesses.")
    content = content.replace('Las Vegas IT consulting, Las Vegas AI consulting, systems integration Las Vegas, ERP implementation, cloud architecture, hospitality technology, AWS, LLM integration Nevada', f"{city['city_name']} IT consulting, {city['city_name']} AI consulting, systems integration {city['short_city']}, ERP implementation, cloud architecture, enterprise tech, AWS, LLM integration")
    
    content = content.replace('Las Vegas IT & AI Consulting | Senior Systems Integration | SZG Labs', f"{city['city_name']} IT & AI Consulting | Senior Systems Integration | SZG Labs")
    content = content.replace('Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"National senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for {city['city_name']} businesses.")
    
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
    content = content.replace('Based in Las Vegas and available for on-site engagements across the metro area.', f"Based in Las Vegas, we provide high-level engagements across {city['region']} when needed.")
    
    content = content.replace('Las Vegas industries we know', f"{city['city_name']} industries we know")
    content = content.replace('growing Las Vegas companies', f"growing {city['short_city']} companies")
    
    content = content.replace('Built for Las Vegas operators', f"Built for {city['city_name']} operators")
    content = content.replace('across Las Vegas, Henderson, Summerlin, and the resort corridor.', f"across {city['region']}.")
    
    # Industries
    content = content.replace('<h3>Hospitality & Gaming</h3>', f"<h3>{city['ind_1_title']}</h3>")
    content = content.replace('<p>From high-volume transaction processing to guest experience personalization, we build secure systems that integrate with property management systems (PMS) and gaming platforms.</p>', f"<p>{city['ind_1_desc']}</p>")
    
    content = content.replace('<h3>Retail & E-Commerce</h3>', f"<h3>{city['ind_2_title']}</h3>")
    content = content.replace('<p>We connect point-of-sale (POS), warehouse management (WMS), and enterprise resource planning (ERP) systems to create unified omnichannel experiences for local and national retailers.</p>', f"<p>{city['ind_2_desc']}</p>")
    
    # FAQ Updates
    content = content.replace('Do you provide on-site IT and AI consulting in Las Vegas?', f"Do you provide IT and AI consulting in {city['city_name']}?")
    content = content.replace('Yes. SZG Labs is locally based in downtown Las Vegas and provides on-site technical consulting, architecture planning, and engineering execution across the entire Las Vegas valley, including Henderson, Summerlin, and the resort corridor.', f"Yes. While headquartered in Las Vegas, we provide dedicated technical consulting, architecture planning, and engineering execution for our {city['city_name']} clients, blending seamless remote engineering with strategic on-site collaboration when required.")
    
    content = content.replace('How does SZG Labs differ from typical Las Vegas managed IT services (MSPs)?', f"How does SZG Labs differ from typical {city['city_name']} managed IT services (MSPs)?")
    content = content.replace('What AI integration solutions do you provide for Las Vegas businesses?', f"What AI integration solutions do you provide for {city['city_name']} businesses?")
    
    content = content.replace('How do we get started with SZG Labs in Las Vegas?', f"How do we get started with SZG Labs in {city['city_name']}?")
    content = content.replace('contact our Las Vegas office at', 'contact our engineering team at')
    
    content = content.replace('Questions about our Las Vegas IT', f"Questions about our {city['city_name']} IT")
    content = content.replace('Know a Las Vegas operator', f"Know a {city['city_name']} operator")
    content = content.replace('Las Vegas, NV 89101', 'Las Vegas, NV 89101') # Keep HQ address
    
    with open(f"/root/projects/agy/szg/{city['filename']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 5 new East Coast pages.")
