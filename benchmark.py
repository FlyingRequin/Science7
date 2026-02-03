import sys
import time
from playwright.sync_api import sync_playwright

def benchmark(port):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        start_time = time.time()
        # Navigate to the page. Time to first byte is part of it, but we care more about rendering.
        # However, page.goto waits for load event by default.
        # We want to measure when the CONTENT appears, which happens after React hydration/rendering.
        page.goto(f"http://localhost:{port}/index.html")

        # Wait for the specific element that indicates the app is running
        page.wait_for_selector("text=BioBuddy", state="visible")

        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Time to interactive: {duration:.2f} ms")

        browser.close()

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else "8000"
    benchmark(port)
