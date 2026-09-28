import re
import json
import os
from datetime import datetime

cities_data = [
    {
        "filename": "reno-it-consulting.html",
        "city_name": "Reno",
        "short_city": "Reno",
        "region": "Reno, Sparks, and Northern Nevada",
        "area_served": '[\n        "Reno",\n        "Sparks",\n        "Carson City",\n        "Fernley",\n        "Lake Tahoe"\n      ]',
        "lat": "39.5296",
        "lon": "-119.8138",
        "region_code": "US-NV",
        "ind_1_title": "Manufacturing & Logistics",
        "ind_1_desc": "We build scalable Odoo ERP implementations and automated data pipelines that connect Tahoe-Reno Industrial Center manufacturers with their global supply chains.",
        "ind_2_title": "Warehouse Automation & AI",
        "ind_2_desc": "We deploy Agentic AI workflows and EDI integrations that eliminate manual order entry and optimize fulfillment operations for fast-growing logistics hubs.",
        "market_desc": "Reno is one of the fastest-growing logistics and advanced manufacturing hubs in the West"
    },
    {
        "filename": "boise-it-consulting.html",
        "city_name": "Boise",
        "short_city": "Boise",
        "region": "Boise and the Treasure Valley",
        "area_served": '[\n        "Boise",\n        "Meridian",\n        "Nampa",\n        "Caldwell",\n        "Eagle"\n      ]',
        "lat": "43.6150",
        "lon": "-116.2023",
        "region_code": "US-ID",
        "ind_1_title": "Tech Manufacturing & Cloud",
        "ind_1_desc": "We support Boise's booming tech sector with senior AWS cloud architecture, DevOps automation, and scalable backend infrastructure.",
        "ind_2_title": "Wholesale & Distribution",
        "ind_2_desc": "We architect Odoo ERP solutions and B2B EDI integrations that streamline complex multi-company operations and warehouse workflows.",
        "market_desc": "Boise is experiencing explosive growth in tech manufacturing and distribution"
    },
    {
        "filename": "greenville-it-consulting.html",
        "city_name": "Greenville",
        "short_city": "Greenville",
        "region": "Greenville and the Upstate",
        "area_served": '[\n        "Greenville",\n        "Spartanburg",\n        "Anderson",\n        "Greer",\n        "Mauldin"\n      ]',
        "lat": "34.8526",
        "lon": "-82.3940",
        "region_code": "US-SC",
        "ind_1_title": "Automotive Supply Chain & Manufacturing",
        "ind_1_desc": "We design high-availability EDI pipelines (850, 856, 810) and robust Odoo ERP environments for tier-1 suppliers and regional manufacturers.",
        "ind_2_title": "Enterprise Data Automation",
        "ind_2_desc": "We replace manual factory and inventory reporting with autonomous AI agents and real-time dashboard integrations that drive operational visibility.",
        "market_desc": "Greenville is a powerhouse of automotive manufacturing and enterprise supply chain operations"
    },
    {
        "filename": "el-paso-it-consulting.html",
        "city_name": "El Paso",
        "short_city": "El Paso",
        "region": "El Paso and the Borderplex",
        "area_served": '[\n        "El Paso",\n        "Las Cruces",\n        "Santa Teresa",\n        "Juarez"\n      ]',
        "lat": "31.7619",
        "lon": "-106.4850",
        "region_code": "US-TX",
        "ind_1_title": "Cross-Border Logistics & 3PL",
        "ind_1_desc": "We build highly secure, fault-tolerant data exchange layers and custom API integrations that synchronize cross-border logistics and customs workflows.",
        "ind_2_title": "Supply Chain ERP Implementation",
        "ind_2_desc": "We specialize in complex multi-currency, multi-warehouse Odoo ERP deployments that unify operations across international trade zones.",
        "market_desc": "El Paso is a critical nexus for international trade, logistics, and manufacturing"
    }
]

with open('/root/projects/agy/szg/las-vegas-it-consulting.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

for city in cities_data:
    content = base_content
    
    # Meta / Title
    content = content.replace('Las Vegas IT & AI Consulting | SZG Labs', f"{city['city_name']} IT & AI Consulting | SZG Labs")
    content = content.replace('Local senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"Regional senior engineers delivering AI systems integration, Odoo ERP implementation, cloud architecture, and data pipelines for {city['city_name']} businesses.")
    content = content.replace('Las Vegas IT consulting, Las Vegas AI consulting, systems integration Las Vegas, ERP implementation, cloud architecture, hospitality technology, AWS, LLM integration Nevada', f"{city['city_name']} IT consulting, {city['city_name']} AI consulting, systems integration {city['short_city']}, Odoo ERP implementation, cloud architecture, logistics tech, AWS, LLM integration")
    
    # Update geo tags properly instead of removing them
    content = re.sub(r'content="US-NV"', f'content="{city["region_code"]}"', content)
    content = re.sub(r'content="Las Vegas, Nevada"', f'content="{city["city_name"]}"', content)
    content = re.sub(r'content="36\.1601;-115\.1465"', f'content="{city["lat"]};{city["lon"]}"', content)
    content = re.sub(r'content="36\.1601, -115\.1465"', f'content="{city["lat"]}, {city["lon"]}"', content)
    content = re.sub(r'"latitude":\s*36\.1601', f'"latitude": {city["lat"]}', content)
    content = re.sub(r'"longitude":\s*-115\.1465', f'"longitude": {city["lon"]}', content)
    
    content = content.replace('Las Vegas IT & AI Consulting | Senior Systems Integration | SZG Labs', f"{city['city_name']} IT, AI & ERP Consulting | Senior Systems Integration")
    content = content.replace('Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.', f"Regional senior engineers delivering AI systems integration, Odoo ERP implementation, and data pipelines for {city['city_name']} businesses.")
    
    content = content.replace('las-vegas-it-consulting.html', city['filename'])
    
    # JSON-LD
    content = content.replace('SZG Labs - Las Vegas IT & AI Consulting', f"SZG Labs - {city['city_name']} IT & AI Consulting")
    
    old_area = r'"areaServed": \[\s*"Las Vegas",\s*"Henderson",\s*"Summerlin",\s*"North Las Vegas",\s*"Paradise",\s*"Spring Valley"\s*\]'
    content = re.sub(old_area, f'"areaServed": {city["area_served"]}', content)
    
    # Body replacements
    content = content.replace('IT & AI Consulting for Las Vegas Businesses', f"IT, AI & ERP Consulting for {city['city_name']} Businesses")
    content = content.replace('across the Las Vegas metro', f"across the {city['city_name']} metro")
    
    content = content.replace('The Las Vegas Advantage', f"The SZG Labs Advantage in {city['city_name']}")
    content = content.replace('Las Vegas is one of the fastest-growing business markets in the country', city['market_desc'])
    content = content.replace('SZG Labs was founded in Las Vegas to fill that gap.', 'SZG Labs brings senior engineering expertise to fill the gaps left by traditional MSP agencies.')
    content = content.replace('alt="Las Vegas skyline at night"', f'alt="{city["city_name"]}"')
    content = content.replace('Based in Las Vegas and available for on-site engagements across the metro area.', f"Based in Las Vegas, we provide on-site engineering engagements across {city['region']} when needed.")
    
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
    content = content.replace('Do you provide on-site IT and AI consulting in Las Vegas?', f"Do you provide on-site IT and ERP consulting in {city['city_name']}?")
    content = content.replace('Yes. SZG Labs is locally based in downtown Las Vegas and provides on-site technical consulting, architecture planning, and engineering execution across the entire Las Vegas valley, including Henderson, Summerlin, and the resort corridor.', f"SZG Labs is headquartered in Las Vegas, just a short flight away. We provide dedicated, on-site technical consulting, architecture planning, and engineering execution for our {city['city_name']} clients when physical presence is required, seamlessly blending remote engineering with strategic on-site collaboration.")
    
    content = content.replace('How does SZG Labs differ from typical Las Vegas managed IT services (MSPs)?', f"How does SZG Labs differ from typical {city['city_name']} managed IT services (MSPs)?")
    content = content.replace('What AI integration solutions do you provide for Las Vegas businesses?', f"What AI and ERP integration solutions do you provide for {city['city_name']} businesses?")
    
    content = content.replace('How do we get started with SZG Labs in Las Vegas?', f"How do we get started with SZG Labs in {city['city_name']}?")
    content = content.replace('contact our Las Vegas office at', 'contact our engineering team at')
    
    content = content.replace('Questions about our Las Vegas IT', f"Questions about our {city['city_name']} IT")
    content = content.replace('Know a Las Vegas operator', f"Know a {city['city_name']} operator")
    
    with open(f"/root/projects/agy/szg/{city['filename']}", 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Generated {len(cities_data)} new city pages.")
