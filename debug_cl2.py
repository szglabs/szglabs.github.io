import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://newyork.craigslist.org/search/ofc?query=data%20entry", wait_until="domcontentloaded")
        content = await page.content()
        with open("ny_sample.html", "w") as f:
            f.write(content)
        await browser.close()
asyncio.run(test())
