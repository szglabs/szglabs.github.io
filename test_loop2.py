import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        leads = []
        url = f"https://newyork.craigslist.org/search/ofc?query=data%20entry"
        await page.goto(url, wait_until="domcontentloaded")
        
        # Craigslist hydrated class: "cl-search-result"
        # Pre-hydrated: "cl-static-search-result"
        # We can just look for 'a.titlestring' or '.title'
        
        links = await page.locator("a.titlestring, a.posting-title").all()
        for link in links[:5]:
            title = await link.inner_text()
            href = await link.get_attribute("href")
            print("-", title, href)
        await browser.close()
asyncio.run(test())
