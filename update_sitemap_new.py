import re

with open('/root/projects/agy/szg/sitemap.xml', 'r') as f:
    content = f.read()

new_sitemap_entries = """  <url>
    <loc>https://szglabs.com/reno-it-consulting.html</loc>
    <lastmod>2026-08-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>
  <url>
    <loc>https://szglabs.com/boise-it-consulting.html</loc>
    <lastmod>2026-08-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>
  <url>
    <loc>https://szglabs.com/greenville-it-consulting.html</loc>
    <lastmod>2026-08-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>
  <url>
    <loc>https://szglabs.com/el-paso-it-consulting.html</loc>
    <lastmod>2026-08-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>
</urlset>"""

if "reno-it-consulting" not in content:
    content = content.replace("</urlset>", new_sitemap_entries)
    with open('/root/projects/agy/szg/sitemap.xml', 'w') as f:
        f.write(content)
    print("Updated sitemap.xml")
else:
    print("sitemap already updated")
