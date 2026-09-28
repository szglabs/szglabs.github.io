import glob

html_files = glob.glob('/root/projects/agy/szg/*.html')

new_links = """            <li><i class="bi bi-chevron-right"></i> <a href="seattle-it-consulting.html">IT & AI Consulting in Seattle</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="phoenix-it-consulting.html">IT & AI Consulting in Phoenix</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="salt-lake-city-it-consulting.html">IT & AI Consulting in Salt Lake City</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="san-francisco-it-consulting.html">IT & AI Consulting in San Francisco</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="austin-it-consulting.html">IT & AI Consulting in Austin</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="dallas-it-consulting.html">IT & AI Consulting in Dallas</a></li>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('<li><i class="bi bi-chevron-right"></i> <a href="seattle-it-consulting.html">IT & AI Consulting in Seattle</a></li>', new_links)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("footer links updated in all html files")
