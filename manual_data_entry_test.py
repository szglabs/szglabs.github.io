import asyncio
from playwright.async_api import async_playwright

async def get_data_entry_leads():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        
        # Search Context (JS Disabled for speed and static DOM)
        search_ctx = await browser.new_context()
        await search_ctx.route("**/*.js", lambda route: route.abort())
        search_page = await search_ctx.new_page()
        
        await search_page.goto("https://newyork.craigslist.org/search/ofc?query=data%20entry")
        items = await search_page.locator("li.cl-static-search-result > a").all()
        
        leads = []
        for item in items[:2]:
            title = await item.locator(".title").inner_text()
            href = await item.get_attribute("href")
            leads.append({"title": title, "link": href})
            
        await search_ctx.close()
        
        # Email Context (JS Enabled to click reply)
        email_ctx = await browser.new_context()
        email_page = await email_ctx.new_page()
        
        print(f"Found {len(leads)} 'data entry' jobs in NYC. Fetching emails...\n")
        
        for lead in leads:
            reply_email = None
            async def on_response(resp):
                nonlocal reply_email
                if "/reply/" in resp.url and resp.url.endswith("/0"):
                    try:
                        data = await resp.json()
                        reply_email = data.get("email")
                    except:
                        pass
            email_page.on("response", on_response)
            
            try:
                await email_page.goto(lead["link"], wait_until="domcontentloaded", timeout=10000)
                btn = email_page.locator("button.reply-button").first
                if await btn.count() > 0:
                    await btn.click()
                    await asyncio.sleep(2.5)
                
                lead["email"] = reply_email if reply_email else "Could not resolve"
                desc = await email_page.locator("#postingbody").inner_text()
                lead["desc"] = desc.replace("\n", " ")[:150]
            except Exception:
                lead["email"] = "Error"
                lead["desc"] = ""
                
            email_page.remove_listener("response", on_response)
            
            print(f"TITLE: {lead['title']}")
            print(f"LINK: {lead['link']}")
            print(f"EMAIL: {lead['email']}")
            print(f"SNIPPET: {lead['desc']}...\n")
            
        await browser.close()

asyncio.run(get_data_entry_leads())
