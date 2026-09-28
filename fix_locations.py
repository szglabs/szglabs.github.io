import re

def fix_file(filepath, city, short_city, region):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. H1 and Hero
    content = content.replace('IT & AI Consulting for Las Vegas Businesses', f'IT & AI Consulting for {city} Businesses')
    content = content.replace('across the Las Vegas metro', f'across the {city} metro')
    
    # 2. Advantage Section
    content = content.replace('The Las Vegas Advantage', f'The SZG Labs Advantage in {city}')
    if city == 'Los Angeles':
        content = content.replace('Las Vegas is one of the fastest-growing business markets in the country', 'Los Angeles is one of the most dynamic business markets in the country')
    else:
        content = content.replace('Las Vegas is one of the fastest-growing business markets in the country', 'Seattle is one of the most innovative tech markets in the country')
        
    content = content.replace('SZG Labs was founded in Las Vegas to fill that gap.', 'SZG Labs brings senior engineering expertise to fill the gaps left by traditional agencies.')
    content = content.replace('alt="Las Vegas skyline at night"', f'alt="{city}"')
    content = content.replace('Based in Las Vegas and available for on-site engagements across the metro area.', f'Based in Las Vegas, we provide on-site engagements across {region} when needed.')
    
    # 3. Industries
    content = content.replace('Las Vegas industries we know', f'{city} industries we know')
    content = content.replace('growing Las Vegas companies', f'growing {short_city} companies')
    
    # 4. Built for...
    content = content.replace('Built for Las Vegas operators', f'Built for {city} operators')
    if city == 'Los Angeles':
        content = content.replace('across Las Vegas, Henderson, Summerlin, and the resort corridor.', 'across Los Angeles, Santa Monica, Irvine, and Southern California.')
    else:
        content = content.replace('across Las Vegas, Henderson, Summerlin, and the resort corridor.', 'across Seattle, Bellevue, Redmond, and the Pacific Northwest.')
    
    # 5. FAQ Header & Footer
    content = content.replace('Questions about our Las Vegas IT', f'Questions about our {city} IT')
    content = content.replace('Know a Las Vegas operator', f'Know a {city} operator')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
fix_file('/root/projects/agy/szg/los-angeles-it-consulting.html', 'Los Angeles', 'LA', 'Los Angeles')
fix_file('/root/projects/agy/szg/seattle-it-consulting.html', 'Seattle', 'Pacific Northwest', 'Seattle and the Pacific Northwest')

print("Fixed")
