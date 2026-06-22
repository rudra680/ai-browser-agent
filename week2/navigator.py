import json
import asyncio
from playwright.async_api import async_playwright


async def navigator():

    try:
        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()

            try:
                await page.goto(
                    "https://news.ycombinator.com",
                    timeout=10000
                )

            except Exception as e:
                print("Navigation Error:", e)
                return

            try:
                titles = await page.locator(
                    ".titleline"
                ).all_text_contents()

            except Exception as e:
                print("Element Error:", e)
                return

            top5 = titles[:5]

            with open(
                "week2/data/news.json",
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    {"titles": top5},
                    file,
                    indent=4
                )

            print("\nTop 5 Titles:\n")

            for title in top5:
                print(title)

            await browser.close()

    except Exception as e:
        print("Unexpected Error:", e)


asyncio.run(navigator())