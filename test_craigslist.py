import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        try:
            await page.goto("https://sfbay.craigslist.org/search/sof", wait_until="domcontentloaded", timeout=15000)
            title = await page.title()
            print("TITLE:", title)
            # Get first 3 job titles
            titles = await page.locator(".title").all_inner_texts()
            print("FOUND TITLES:", titles[:3])
        except Exception as e:
            print("ERROR:", e)
        finally:
            await browser.close()

asyncio.run(test())
