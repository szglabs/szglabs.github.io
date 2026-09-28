with open('/root/projects/agy/szglabs_lead_scraper.py', 'r') as f:
    code = f.read()

email_import = "import smtplib, ssl\nfrom email.message import EmailMessage\n"
if "smtplib" not in code:
    code = code.replace("import asyncio", email_import + "import asyncio")

email_logic = """
    filename = f"/root/leads_outreach_drafts_final.md"
    with open(filename, "w") as f:
        f.write(report)
        
    print(f"Report saved to {filename}")

    # Send the email
    print("Sending report via email...")
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
        print(f"Failed to send email: {e}")
"""

# Replace the end of main() with the new email logic
code = code.split('filename = f"/root/leads_outreach_drafts_final.md"')[0] + email_logic

with open('/root/projects/agy/szglabs_lead_scraper.py', 'w') as f:
    f.write(code)
