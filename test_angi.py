import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        print("Testing Yelp...")
        try:
            await page.goto("https://www.yelp.com/search?find_desc=General+Contractors&find_loc=San+Francisco%2C+CA", wait_until="domcontentloaded", timeout=10000)
            print("YELP TITLE:", await page.title())
        except Exception as e: print("Yelp Error:", e)
            
        print("Testing Angi...")
        try:
            await page.goto("https://www.angi.com/companylist/san-francisco/general-contractors.htm", wait_until="domcontentloaded", timeout=10000)
            print("ANGI TITLE:", await page.title())
        except Exception as e: print("Angi Error:", e)
        
        await browser.close()

asyncio.run(test())
