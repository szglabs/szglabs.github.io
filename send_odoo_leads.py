import smtplib, ssl, markdown
from email.message import EmailMessage
from datetime import datetime

md_content = """# Odoo Rescue Leads - Reddit 

Here are the 3 high-intent Odoo leads discovered by the subagent.

## 1. "Odoo is driving me insane"
* **Source / URL:** [View Reddit Post](https://www.reddit.com/r/smallbusiness/comments/1q9pk5b/odoo_is_driving_me_insane/)
* **Pain Point:** The user is trying to automate their operations as much as possible but is completely overwhelmed by Odoo's complexity, leading to deep frustration ("driving me insane").

### Draft Outreach Message
```text
Hi there, I saw your post about Odoo driving you insane while trying to automate your business operations. As a Senior Architect at SZG Labs, I step into frustrating Odoo environments every day to untangle the mess and properly automate workflows without the bloated overhead of traditional agencies. Let's get on a brief call so I can show you exactly how we can get your system running smoothly and reliably.

Best,
Christopher O'Neal
Managing Member, SZG Labs
christopher.oneal@szglabs.com
702-530-3254
```

---

## 2. "Thoughts on SYSPRO vs Odoo ERP Systems?"
* **Source / URL:** [View Reddit Post](https://www.reddit.com/r/smallbusiness/comments/1ry8hfi/thoughts_on_syspro_vs_odoo_erp_systems/)
* **Pain Point:** A manufacturing company is considering migrating from their legacy SYSPRO system to Odoo but needs expert guidance to ensure a smooth transition and proper implementation.

### Draft Outreach Message
```text
Hi there, I noticed your manufacturing company is considering a migration from SYSPRO to Odoo and you're seeking guidance. At SZG Labs, I specialize as a Senior Architect in implementing and customizing Odoo for complex manufacturing operations, delivering high-level expertise without the bloated overhead of a massive agency. I'd love to chat about your specific requirements and ensure your potential transition to Odoo is a resounding success.

Best,
Christopher O'Neal
Managing Member, SZG Labs
christopher.oneal@szglabs.com
702-530-3254
```

---

## 3. "Odoo? My First Small Business issue"
* **Source / URL:** [View Reddit Post](https://www.reddit.com/r/smallbusiness/comments/1qdmjhc/odoo_my_first_small_business_issue/)
* **Pain Point:** A former service industry professional is launching their first small business and has immediately run into technical roadblocks trying to get their initial Odoo setup working.

### Draft Outreach Message
```text
Hi there, I saw your post about starting your first small business and running into early issues setting up Odoo. I operate as a Senior Architect at SZG Labs where I rescue and implement Odoo systems for business owners, providing top-tier technical guidance without the bloated overhead of typical agencies. I would be happy to step in and handle the technical heavy lifting so you can focus entirely on launching and growing your new business.

Best,
Christopher O'Neal
Managing Member, SZG Labs
christopher.oneal@szglabs.com
702-530-3254
```
"""

# Save as MD
with open('/root/odoo_reddit_leads.md', 'w') as f:
    f.write(md_content)

# Send HTML Email
html_body = markdown.markdown(md_content, extensions=['fenced_code', 'nl2br'])
styled_html = f"""
<html>
<head>
<style>
    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
    h1 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
    h2 {{ color: #34495e; margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
    ul {{ list-style-type: none; padding-left: 0; }}
    li {{ margin-bottom: 10px; padding: 10px; background: #f9f9f9; border-left: 4px solid #e67e22; }}
    a {{ color: #e67e22; text-decoration: none; font-weight: bold; }}
    a:hover {{ text-decoration: underline; }}
    pre {{ background: #f4f4f4; border-left: 4px solid #2ecc71; padding: 15px; overflow-x: auto; white-space: pre-wrap; font-family: monospace; font-size: 14px; margin-top: 15px; }}
    code {{ font-family: monospace; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

try:
    msg = EmailMessage()
    msg.set_content(md_content)
    msg.add_alternative(styled_html, subtype='html')
    msg["Subject"] = f"SZG Labs Odoo Rescue Leads - {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = "christopher.oneal@szglabs.com"
    msg["To"] = "christopher.oneal@szglabs.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
        server.login("christopher.oneal@szglabs.com", "90()opOPl;L:")
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
