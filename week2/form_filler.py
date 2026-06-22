import json
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def form_filler():

    data_file = Path(__file__).parent / "data" / "user.json"

    with open(data_file, "r") as file:
        user = json.load(file)

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page()

        try:
            await page.goto(
                "https://demoqa.com/automation-practice-form",
                timeout=10000
            )

            # First Name
            await page.fill(
                "#firstName",
                user["firstName"]
            )

            # Last Name
            await page.fill(
                "#lastName",
                user["lastName"]
            )

            # Email
            await page.fill(
                "#userEmail",
                user["email"]
            )

            # Gender
            await page.get_by_text(
                user["gender"],
                exact=True
            ).click()

            # Mobile
            await page.fill(
                "#userNumber",
                user["mobile"]
            )

            # Subject
            await page.fill(
                "#subjectsInput",
                user["subject"]
            )

            await page.keyboard.press("Enter")

            # Hobby
            await page.get_by_text(
                user["hobby"],
                exact=True
            ).click()

            # Address
            await page.fill(
                "#currentAddress",
                user["address"]
            )

            # State
            await page.locator("#state").click()

            await page.keyboard.type(
                user["state"]
            )

            await page.keyboard.press(
                "Enter"
            )

            # City
            await page.locator("#city").click()

            await page.keyboard.type(
                user["city"]
            )

            await page.keyboard.press(
                "Enter"
            )

            # Screenshot before submit
            screenshot_path = (
                Path(__file__).parent
                / "screenshots"
                / "filled_form.png"
            )

            await page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print("Screenshot saved")

        except Exception as e:
            print("Error:", e)

        finally:
            await page.wait_for_timeout(3000)
            await browser.close()


asyncio.run(form_filler())