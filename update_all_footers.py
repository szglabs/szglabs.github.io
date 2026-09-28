import os
import glob

# The links we want to add
new_links = """            <li><i class="bi bi-chevron-right"></i> <a href="reno-it-consulting.html">IT & AI Consulting in Reno</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="boise-it-consulting.html">IT & AI Consulting in Boise</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="greenville-it-consulting.html">IT & AI Consulting in Greenville</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="el-paso-it-consulting.html">IT & AI Consulting in El Paso</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="security.html">Security</a></li>"""

# We will replace the start of the legal links with our new links + the legal link
target_pattern = '            <li><i class="bi bi-chevron-right"></i> <a href="security.html">Security</a></li>'

html_files = glob.glob('/root/projects/agy/szg/*.html')
count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "reno-it-consulting.html" not in content and target_pattern in content:
        content = content.replace(target_pattern, new_links)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated footers in {count} HTML files.")
