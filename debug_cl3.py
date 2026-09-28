import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://newyork.craigslist.org/search/ofc", wait_until="domcontentloaded")
        titles = await page.locator(".title").all_inner_texts()
        print(f"Found {len(titles)} titles in NYC ofc")
        for t in titles[:5]:
            print("-", t)
        await browser.close()
asyncio.run(test())
