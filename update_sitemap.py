with open('/root/projects/agy/szg/sitemap.xml', 'r') as f:
    content = f.read()

new_entry = """  <url>
    <loc>https://szglabs.com/los-angeles-it-consulting.html</loc>
    <lastmod>2026-08-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>
</urlset>"""

content = content.replace('</urlset>', new_entry)

with open('/root/projects/agy/szg/sitemap.xml', 'w') as f:
    f.write(content)
print("sitemap updated")
