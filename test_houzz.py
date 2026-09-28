import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        print("Loading Houzz...")
        await page.goto("https://www.houzz.com/professionals/general-contractor/c/San-Francisco--CA", wait_until="domcontentloaded", timeout=20000)
        
        # Houzz often uses a class like 'hz-pro-search-result' or similar. 
        # Let's just grab all links that have 'pro' in the href and see what we get.
        links = await page.locator("a[href*='/pro/']").all()
        print(f"Found {len(links)} pro links.")
        for link in links[:5]:
            href = await link.get_attribute("href")
            text = await link.inner_text()
            if text.strip():
                print(f"- {text.strip().split(chr(10))[0]}: {href}")
        
        await browser.close()

asyncio.run(test())
