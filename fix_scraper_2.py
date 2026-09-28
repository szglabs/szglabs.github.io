import re
with open('/root/projects/agy/szglabs_lead_scraper.py', 'r') as f:
    code = f.read()

# Remove the broken loop
part1 = code.split('for i, lead in enumerate(leads):')[0]
part2 = code.split('filename = f"/root/leads_outreach_drafts_final.md"')[1]

new_loop = """    for i, lead in enumerate(leads):
        draft = generate_draft(lead)
        report += f"## {i+1}. {lead['title']}\\n"
        report += f"* **City:** {lead['city']}\\n"
        report += f"* **URL:** [View Posting]({lead['link']})\\n"
        report += f"* **Send To:** {lead['email']}\\n"
        report += f"* **Score:** {lead['score']}\\n"
        report += f"* **Snippet:** {lead['description']}...\\n\\n"
        report += f"### Draft Email\\n```text\\n{draft}\\n```\\n\\n"
        report += "---\\n\\n"

    filename = f"/root/leads_outreach_drafts_final.md"
"""

with open('/root/projects/agy/szglabs_lead_scraper.py', 'w') as f:
    f.write(part1 + new_loop + part2)
