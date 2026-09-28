import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        leads = []
        for city in ["newyork", "sfbay"]:
            url = f"https://{city}.craigslist.org/search/ofc?query=data%20entry"
            print("Loading", url)
            await page.goto(url, wait_until="networkidle") # Wait for JS
            job_elements = await page.locator("li.cl-static-search-result").all()
            print("Found elements:", len(job_elements))
            for job in job_elements[:5]:
                try:
                    title = await job.locator(".title").inner_text()
                    print("  - Title:", title)
                    leads.append(title)
                except Exception as e:
                    print("  - Error:", e)
        print("Total leads:", len(leads))
        await browser.close()
asyncio.run(test())
