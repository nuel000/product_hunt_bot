from playwright.sync_api import Playwright, sync_playwright
import time
import sys

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(50000)
    page.goto("https://www.producthunt.com/")
    
    print("Navigating to Product Hunt...")
    sys.stdout.flush()

    with page.expect_popup() as page1_info:
        page.frame_locator("iframe[title=\"Sign in with Google Dialogue\"]").get_by_role("button", name="Continue").click()
    
    time.sleep(10)
    page1 = page1_info.value
    print("Popup opened, attempting to log in...")
    sys.stdout.flush()

    time.sleep(3)
    page1.get_by_label("Email or phone").fill("momohemmanuel073")
    print("Email entered.")
    sys.stdout.flush()

    time.sleep(3)
    page1.get_by_role("button", name="Next").click()
    print("Next button clicked.")
    sys.stdout.flush()

    time.sleep(3)
    page1.get_by_label("Enter your password").click(modifiers=["Control"])
    time.sleep(3)
    page1.get_by_label("Enter your password").click()
    time.sleep(3)
    page1.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
    print("Password entered.")
    sys.stdout.flush()

    time.sleep(3)
    page1.get_by_role("button", name="Next").click()
    print("Logging in...")
    sys.stdout.flush()

    time.sleep(25)
    print("Logged in to Product Hunt.")
    sys.stdout.flush()

    # Click the first button
    first_button = page.wait_for_selector('xpath=//*[@id="root-container"]/div[1]/main/div[2]/div/div[1]/div[2]/button/div/div[1]', timeout=10000)
    if first_button:
        page.locator('xpath=//*[@id="root-container"]/div[1]/main/div[2]/div/div[1]/div[2]/button/div/div[1]').click()
        print("First button clicked.")
    else:
        print("First button not found!")
    sys.stdout.flush()

    time.sleep(3)
    
    # Click the second button
    second_button = page.wait_for_selector('xpath=//*[@id="root-container"]/div[1]/main/div/div/div[1]/div[3]/button/div/div[1]', timeout=10000)
    if second_button:
        page.locator('xpath=//*[@id="root-container"]/div[1]/main/div/div/div[1]/div[3]/button/div/div[1]').click()
        print("Second button clicked.")
    else:
        print("Second button not found!")
    sys.stdout.flush()

    time.sleep(10)
    
    # Close the browser
    context.close()
    browser.close()
    print("Browser closed.")
    sys.stdout.flush()


with sync_playwright() as playwright:
    run(playwright)
