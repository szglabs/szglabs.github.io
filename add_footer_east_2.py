import glob, re

html_files = glob.glob('/root/projects/agy/szg/*.html')

new_links = """            <li><i class="bi bi-chevron-right"></i> <a href="new-york-it-consulting.html">IT & AI Consulting in NYC</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="boston-it-consulting.html">IT & AI Consulting in Boston</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="washington-dc-it-consulting.html">IT & AI Consulting in Washington D.C.</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="atlanta-it-consulting.html">IT & AI Consulting in Atlanta</a></li>
            <li><i class="bi bi-chevron-right"></i> <a href="miami-it-consulting.html">IT & AI Consulting in Miami</a></li>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<li><i class="bi bi-chevron-right"></i> <a href="dallas-it-consulting\.html">.*?</a></li>)'
    content = re.sub(pattern, r'\1\n' + new_links, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("footer links updated in all html files again")
