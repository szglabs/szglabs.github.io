import re
with open('/root/projects/agy/szglabs_lead_scraper.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "report += f\"## {i+1}. {lead['title']}\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"* **City:** {lead['city']}\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"* **URL:** [View Posting]({lead['link']})\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"* **Send To:** {lead['email']}\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"* **Score:** {lead['score']}\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"* **Snippet:** {lead['description']}...\\" in line:
        line = line.replace("\\\n", "\\n\"")
    if "report += f\"### Draft Email\\" in line:
        line = line.replace("\\\n```text\\\n{draft}\\\n```\\\n\\\n\"", "\\n```text\\n{draft}\\n```\\n\\n\"")
    if "report += \"---\\" in line:
        line = line.replace("\\\n\\\n\"", "\\n\\n\"")
    new_lines.append(line)

with open('/root/projects/agy/szglabs_lead_scraper.py', 'w') as f:
    f.writelines(new_lines)
