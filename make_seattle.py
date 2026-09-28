import re, json

with open('/root/projects/agy/szg/seattle-it-consulting.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Meta and Headings
content = content.replace(
    '<title>Los Angeles IT & AI Consulting | SZG Labs</title>',
    '<title>Seattle IT & AI Consulting | SZG Labs</title>'
)
content = content.replace(
    '<meta name="description" content="Senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles and Southern California businesses.">',
    '<meta name="description" content="Senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Seattle and Pacific Northwest businesses.">'
)
content = content.replace(
    '<meta name="keywords" content="Los Angeles IT consulting, Los Angeles AI consulting, systems integration LA, ERP implementation, cloud architecture, media technology, e-commerce IT, AWS, LLM integration California">',
    '<meta name="keywords" content="Seattle IT consulting, Seattle AI consulting, systems integration Seattle, ERP implementation, cloud architecture, tech consulting, e-commerce IT, AWS, LLM integration Washington">'
)
content = content.replace(
    '<meta property="og:title" content="Los Angeles IT & AI Consulting | Senior Systems Integration | SZG Labs">',
    '<meta property="og:title" content="Seattle IT & AI Consulting | Senior Systems Integration | SZG Labs">'
)
content = content.replace(
    '<meta property="og:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles businesses.">',
    '<meta property="og:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Seattle businesses.">'
)
content = content.replace(
    '<meta name="twitter:title" content="Los Angeles IT & AI Consulting | Senior Systems Integration | SZG Labs">',
    '<meta name="twitter:title" content="Seattle IT & AI Consulting | Senior Systems Integration | SZG Labs">'
)
content = content.replace(
    '<meta name="twitter:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Los Angeles businesses.">',
    '<meta name="twitter:description" content="Regional senior engineers delivering AI systems integration, ERP implementation, cloud architecture, and data pipelines for Seattle businesses.">'
)
content = content.replace('los-angeles-it-consulting.html', 'seattle-it-consulting.html')

# JSON-LD Adjustments
content = content.replace('"name": "SZG Labs - Los Angeles IT & AI Consulting"', '"name": "SZG Labs - Seattle IT & AI Consulting"')

# Area Served JSON-LD
old_area = r'"areaServed": [\n\s*"Los Angeles",\n\s*"Santa Monica",\n\s*"Irvine",\n\s*"Orange County",\n\s*"Pasadena",\n\s*"Glendale"\n\s*]'
new_area = r'"areaServed": [\n        "Seattle",\n        "Bellevue",\n        "Redmond",\n        "Kirkland",\n        "Tacoma",\n        "Everett"\n      ]'
content = re.sub(old_area, new_area, content)

# Body Text Replacements
content = content.replace('<h1>IT & AI Consulting for Los Angeles Businesses</h1>', '<h1>IT & AI Consulting for Seattle Businesses</h1>')
content = content.replace('partner for Los Angeles enterprises', 'partner for Seattle enterprises')
content = content.replace('Senior engineering capacity serving the Los Angeles market.', 'Senior engineering capacity serving the Seattle and Pacific Northwest market.')
content = content.replace('In a dynamic, fast-paced market like LA', 'In a highly technical and innovative market like Seattle')
content = content.replace('most Los Angeles IT', 'most Seattle IT')

# Industries
content = content.replace('Entertainment & Media', 'Technology & SaaS Platforms')
content = content.replace('From high-volume content delivery networks to personalized audience engagement, we build secure systems that integrate with media asset management and streaming platforms.', 'From high-availability cloud infrastructure to custom product features, we build scalable backends and APIs that help growing software companies accelerate their roadmaps.')

content = content.replace('omnichannel experiences for LA-based consumer brands.', 'omnichannel experiences for Pacific Northwest retail brands.')

content = content.replace('Aerospace & Manufacturing', 'Aerospace, Maritime & Logistics')
content = content.replace('We design complex integration layers and secure data pipelines that sync suppliers, shop floor operations, and ERP systems (like Odoo) to optimize production and ensure compliance.', 'We design complex integration layers and secure data pipelines that sync global suppliers, port operations, and ERP systems (like Odoo) to optimize production and logistics workflows.')

# FAQ Updates
content = content.replace('Do you provide on-site IT and AI consulting in Los Angeles?', 'Do you provide on-site IT and AI consulting in Seattle?')
content = content.replace('SZG Labs is headquartered in Las Vegas, just a short flight away. We provide dedicated, on-site technical consulting, architecture planning, and engineering execution for our Los Angeles clients', 'SZG Labs is headquartered in Las Vegas, just a short flight away. We provide dedicated, on-site technical consulting, architecture planning, and engineering execution for our Seattle and Pacific Northwest clients')

content = content.replace('How does SZG Labs differ from typical Los Angeles managed IT services (MSPs)?', 'How does SZG Labs differ from typical Seattle managed IT services (MSPs)?')
content = content.replace('What AI integration solutions do you provide for Los Angeles businesses?', 'What AI integration solutions do you provide for Seattle businesses?')

content = content.replace('How do we get started with SZG Labs in Los Angeles?', 'How do we get started with SZG Labs in Seattle?')

with open('/root/projects/agy/szg/seattle-it-consulting.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Seattle Page generated successfully.")
