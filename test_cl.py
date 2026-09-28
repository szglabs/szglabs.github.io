import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://sfbay.craigslist.org/search/sof", wait_until="domcontentloaded")
        content = await page.content()
        with open("cl_sample.html", "w") as f:
            f.write(content)
        await browser.close()
asyncio.run(test())
