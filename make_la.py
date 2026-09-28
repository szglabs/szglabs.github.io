import re, json

with open('/root/projects/agy/szg/los-angeles-it-consulting.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Meta and Headings
content = content.replace(
    '<title>Las Vegas IT & AI Consulting | SZG Labs</title>',
    '<title>Los Angeles IT & AI Consulting | SZG Labs</title>'
)
content = content.replace(
    '<meta name="description" content="Local senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.">',
    '<meta name="description" content="Senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles and Southern California businesses.">'
)
content = content.replace(
    '<meta name="keywords" content="Las Vegas IT consulting, Las Vegas AI consulting, systems integration Las Vegas, ERP implementation, cloud architecture, hospitality technology, AWS, LLM integration Nevada">',
    '<meta name="keywords" content="Los Angeles IT consulting, Los Angeles AI consulting, systems integration LA, ERP implementation, cloud architecture, media technology, e-commerce IT, AWS, LLM integration California">'
)
content = content.replace(
    '<meta property="og:title" content="Las Vegas IT & AI Consulting | Senior Systems Integration | SZG Labs">',
    '<meta property="og:title" content="Los Angeles IT & AI Consulting | Senior Systems Integration | SZG Labs">'
)
content = content.replace(
    '<meta property="og:description" content="Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.">',
    '<meta property="og:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles businesses.">'
)
content = content.replace(
    '<meta name="twitter:title" content="Las Vegas IT & AI Consulting | Senior Systems Integration | SZG Labs">',
    '<meta name="twitter:title" content="Los Angeles IT & AI Consulting | Senior Systems Integration | SZG Labs">'
)
content = content.replace(
    '<meta name="twitter:description" content="Local, on-site senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Las Vegas businesses.">',
    '<meta name="twitter:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles businesses.">'
)
content = content.replace('las-vegas-it-consulting.html', 'los-angeles-it-consulting.html')

# Remove geo meta tags since physical address is Vegas, but target is LA.
content = re.sub(r'<meta name="geo\.region" content="US-NV">\n?', '', content)
content = re.sub(r'<meta name="geo\.placename" content="Las Vegas, Nevada">\n?', '', content)
content = re.sub(r'<meta name="geo\.position" content="36\.1601;-115\.1465">\n?', '', content)
content = re.sub(r'<meta name="ICBM" content="36\.1601, -115\.1465">\n?', '', content)

# JSON-LD Adjustments
content = content.replace('"name": "SZG Labs - Las Vegas IT & AI Consulting"', '"name": "SZG Labs - Los Angeles IT & AI Consulting"')

# Remove geo block from JSON-LD
content = re.sub(r'"geo":\s*{\s*"@type":\s*"GeoCoordinates",\s*"latitude":\s*36\.1601,\s*"longitude":\s*-115\.1465\s*},', '', content)

# Area Served JSON-LD
old_area = r'"areaServed": \[\s*"Las Vegas",\s*"Henderson",\s*"Summerlin",\s*"North Las Vegas",\s*"Paradise",\s*"Spring Valley"\s*\]'
new_area = r'"areaServed": [\n        "Los Angeles",\n        "Santa Monica",\n        "Irvine",\n        "Orange County",\n        "Pasadena",\n        "Glendale"\n      ]'
content = re.sub(old_area, new_area, content)

# Body Text Replacements
content = content.replace('<h1>IT & AI Consulting for Las Vegas Businesses</h1>', '<h1>IT & AI Consulting for Los Angeles Businesses</h1>')
content = content.replace('partner for Las Vegas enterprises', 'partner for Los Angeles enterprises')
content = content.replace('Senior engineering capacity for the Las Vegas market.', 'Senior engineering capacity serving the Los Angeles market.')
content = content.replace('In a city that runs 24/7', 'In a dynamic, fast-paced market like LA')
content = content.replace('most Las Vegas IT', 'most Los Angeles IT')

# Industries
content = content.replace('Hospitality & Gaming', 'Entertainment & Media')
content = content.replace('From high-volume transaction processing to guest experience personalization, we build secure systems that integrate with property management systems (PMS) and gaming platforms.', 'From high-volume content delivery networks to personalized audience engagement, we build secure systems that integrate with media asset management and streaming platforms.')

content = content.replace('Retail & E-Commerce', 'Retail & E-Commerce') # keep title
content = content.replace('We connect point-of-sale (POS), warehouse management (WMS), and enterprise resource planning (ERP) systems to create unified omnichannel experiences for local and national retailers.', 'We connect point-of-sale (POS), warehouse management (WMS), and enterprise resource planning (ERP) systems to create unified omnichannel experiences for LA-based consumer brands.')

content = content.replace('Logistics & Supply Chain', 'Aerospace & Manufacturing')
content = content.replace('Vegas is a logistics hub. We design EDI (850, 856, 810) and API integration layers that sync 3PL providers, suppliers, and ERP systems (like Odoo) to eliminate manual data entry.', 'We design complex integration layers and secure data pipelines that sync suppliers, shop floor operations, and ERP systems (like Odoo) to optimize production and ensure compliance.')

# FAQ Updates
content = content.replace('Do you provide on-site IT and AI consulting in Las Vegas?', 'Do you provide on-site IT and AI consulting in Los Angeles?')
content = content.replace('Yes. SZG Labs is locally based in downtown Las Vegas and provides on-site technical consulting, architecture planning, and engineering execution across the entire Las Vegas valley, including Henderson, Summerlin, and the resort corridor.', 'SZG Labs is headquartered in Las Vegas, just a short flight away. We provide dedicated, on-site technical consulting, architecture planning, and engineering execution for our Los Angeles clients when physical presence is required, seamlessly blending remote engineering with strategic on-site collaboration.')

content = content.replace('How does SZG Labs differ from typical Las Vegas managed IT services (MSPs)?', 'How does SZG Labs differ from typical Los Angeles managed IT services (MSPs)?')
content = content.replace('What AI integration solutions do you provide for Las Vegas businesses?', 'What AI integration solutions do you provide for Los Angeles businesses?')

content = content.replace('How do we get started with SZG Labs in Las Vegas?', 'How do we get started with SZG Labs in Los Angeles?')
content = content.replace('contact our Las Vegas office at', 'contact our engineering team at')


with open('/root/projects/agy/szg/los-angeles-it-consulting.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("LA Page generated successfully.")
