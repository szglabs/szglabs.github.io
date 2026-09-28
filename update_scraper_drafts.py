import re

with open('/root/projects/agy/szglabs_lead_scraper.py', 'r') as f:
    code = f.read()

import_block = "import subprocess\n"
if "import subprocess" not in code:
    code = code.replace("import asyncio", import_block + "import asyncio")

drafting_func = """
def generate_draft(lead):
    print(f"Generating draft email for {lead['title']}...")
    prompt = f\"\"\"Write a direct, professional cold outreach email to someone hiring for this role: {lead['title']}. 
Job snippet: {lead['description']}

Rules:
- If this is a manual/data entry role, pitch SZG Labs as building AI systems that replace repetitive human tasks so they don't need to hire admin headcount.
- If this is an engineering/logistics role, pitch Christopher O'Neal as an independent Senior Architect who can execute their ERP/automation roadmap immediately without agency overhead.
- Keep it to 3 sentences. One specific observation, one clear offer, one call to action.
- End the email with this exact signature:
Christopher O'Neal
Managing Member, SZG Labs, LLC
(702) 530-3254
christopher@szglabs.com

To opt out of future emails, reply with "unsubscribe" and I will remove you promptly.
\"\"\"
    try:
        result = subprocess.run(
            ['/root/.local/bin/agy', '--prompt', prompt, '--dangerously-skip-permissions', '/root/projects/agy'],
            capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error generating draft: {e}"
"""

# Insert the drafting function before main()
code = code.replace("def main():", drafting_func + "\ndef main():")

# Update the reporting loop to include the draft
report_loop = """
    for i, lead in enumerate(leads):
        draft = generate_draft(lead)
        
        report += f"## {i+1}. {lead['title']}\\n"
        report += f"* **City:** {lead['city']}\\n"
        report += f"* **URL:** [View Posting]({lead['link']})\\n"
        report += f"* **Send To:** {lead['email']}\\n"
        report += f"* **Score:** {lead['score']}\\n"
        report += f"* **Snippet:** {lead['description']}...\\n\\n"
        report += f"### Draft Email\\n```text\\n{draft}\\n```\\n\\n"
        report += "---\\n\\n"
"""

code = re.sub(r'for i, lead in enumerate\(leads\):.*?report \+= "---\\n\\n"', report_loop, code, flags=re.DOTALL)

with open('/root/projects/agy/szglabs_lead_scraper.py', 'w') as f:
    f.write(code)
