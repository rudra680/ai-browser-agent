import asyncio
from playwright.async_api import async_playwright


async def open_tab(browser, url):

    try:
        page = await browser.new_page()

        await page.goto(
            url,
            timeout=10000
        )

        title = await page.title()

        print(f"\n{url}")
        print(f"Title: {title}")

        return page

    except Exception as e:

        print(f"Error opening {url}: {e}")
        return None


async def tab_manager():

    urls = [
        "https://google.com",
        "https://github.com",
        "https://openai.com",
        "https://stackoverflow.com",
        "https://news.ycombinator.com"
    ]

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        pages = await asyncio.gather(
            *[open_tab(browser, url) for url in urls]
        )

        pages = [page for page in pages if page]

        print("\nAll tabs opened.")

        await asyncio.sleep(5)

        for page in pages[1:]:

            try:
                await page.close()

            except Exception as e:
                print("Close Error:", e)

        print("\nClosed all tabs except the first.")

        await asyncio.sleep(3)

        await browser.close()


asyncio.run(tab_manager())