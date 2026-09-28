with open('/root/projects/agy/szg/sitemap.xml', 'r') as f:
    content = f.read()

urls = [
    "new-york-it-consulting.html",
    "boston-it-consulting.html",
    "washington-dc-it-consulting.html",
    "atlanta-it-consulting.html",
    "miami-it-consulting.html"
]

new_entries = ""
for url in urls:
    new_entries += f"""  <url>
    <loc>https://szglabs.com/{url}</loc>
    <lastmod>2026-08-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>\n"""

new_entries += "</urlset>"

content = content.replace('</urlset>', new_entries)

with open('/root/projects/agy/szg/sitemap.xml', 'w') as f:
    f.write(content)
print("sitemap updated with East Coast cities")
