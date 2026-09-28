import re

with open('/root/projects/agy/leads/szglabs_lead_scraper.py', 'r') as f:
    code = f.read()

# 1. Update the signature in the prompt
old_sig = """Christopher O'Neal
Managing Member, SZG Labs, LLC
(702) 530-3254
christopher@szglabs.com"""

new_sig = """Christopher O'Neal
Managing Member, SZG Labs, LLC
930 S 4th St, Ste 209 #6239
Las Vegas, NV 89101
(702) 530-3254
christopher.oneal@szglabs.com
https://szglabs.com"""

code = code.replace(old_sig, new_sig)

# 2. Update the email sending logic to use HTML
if "import markdown" not in code:
    code = code.replace("import smtplib", "import markdown\nimport smtplib")

old_email = """    print("Sending report via email...")
    try:
        msg = EmailMessage()
        msg.set_content(report)
        msg["Subject"] = f"SZG Labs Lead Report - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = "christopher.oneal@szglabs.com"
        msg["To"] = "christopher.oneal@szglabs.com"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
            server.login("christopher.oneal@szglabs.com", "90()opOPl;L:")
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")"""

new_email = """    print("Sending report via HTML email...")
    try:
        msg = EmailMessage()
        msg.set_content(report) # Plain text fallback
        
        # Convert Markdown to HTML
        html_body = markdown.markdown(report, extensions=['fenced_code', 'nl2br'])
        # Add basic styling to make it look professional
        styled_html = f\"\"\"
        <html>
        <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
            h2 {{ color: #34495e; margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
            ul {{ list-style-type: none; padding-left: 0; }}
            li {{ margin-bottom: 10px; padding: 10px; background: #f9f9f9; border-left: 4px solid #3498db; }}
            a {{ color: #3498db; text-decoration: none; font-weight: bold; }}
            a:hover {{ text-decoration: underline; }}
            pre {{ background: #f4f4f4; border-left: 4px solid #2ecc71; padding: 15px; overflow-x: auto; white-space: pre-wrap; font-family: monospace; font-size: 14px; margin-top: 15px; }}
            code {{ font-family: monospace; }}
            strong {{ color: #2c3e50; }}
        </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        \"\"\"
        msg.add_alternative(styled_html, subtype='html')
        
        msg["Subject"] = f"SZG Labs Lead Report - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = "christopher.oneal@szglabs.com"
        msg["To"] = "christopher.oneal@szglabs.com"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
            server.login("christopher.oneal@szglabs.com", "90()opOPl;L:")
            server.send_message(msg)
        print("HTML Email sent successfully!")
    except Exception as e:
        print(f"Failed to send HTML email: {e}")"""

code = code.replace(old_email, new_email)

with open('/root/projects/agy/leads/szglabs_lead_scraper.py', 'w') as f:
    f.write(code)
