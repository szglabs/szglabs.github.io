import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        
        # Block JavaScript to prevent hydration!
        await context.route("**/*.js", lambda route: route.abort())
        
        page = await context.new_page()
        await page.goto("https://newyork.craigslist.org/search/ofc?query=data%20entry")
        
        items = await page.locator("li.cl-static-search-result > a").all()
        print("Found items:", len(items))
        for item in items[:3]:
            title = await item.locator(".title").inner_text()
            href = await item.get_attribute("href")
            print(f"- {title}: {href}")
            
        await browser.close()
asyncio.run(test())
