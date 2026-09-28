import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://www.houzz.com/professionals/general-contractor/c/San-Francisco--CA", wait_until="domcontentloaded", timeout=20000)
        title = await page.title()
        print("TITLE:", title)
        
        # Get all heading texts
        headings = await page.locator("h3, h2").all_inner_texts()
        print("HEADINGS:", headings[:5])
        
        await browser.close()

asyncio.run(test())
