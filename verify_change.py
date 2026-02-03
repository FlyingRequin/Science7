from playwright.sync_api import sync_playwright
import os

def verify(port):
    os.makedirs("/home/jules/verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(f"http://localhost:{port}/index.html")
        page.wait_for_selector("text=BioBuddy")

        # Take a screenshot
        screenshot_path = "/home/jules/verification/verification.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify(5173)
