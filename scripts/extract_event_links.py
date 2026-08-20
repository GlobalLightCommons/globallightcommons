from playwright.sync_api import sync_playwright

URL = "https://globallightcommons.org/events"

TARGETS = [
    "Register Now",
    "Learn More About LightLogR",
    "View Presentation Slides",
    "Visit lightforpublichealth.org",
    "View Event Details",
    "View Workshop Materials",
    "View Launch Photos",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto(URL, wait_until="networkidle", timeout=60000)

    print("\nEvent links:\n")

    for text in TARGETS:
        locator = page.get_by_text(text, exact=True)

        if locator.count() == 0:
            print(f"{text}: NOT FOUND")
            continue

        element = locator.first

        # The text may itself be the <a>, or be nested inside one.
        href = element.get_attribute("href")

        if not href:
            href = element.evaluate(
                """
                el => {
                    const a = el.closest('a') || el.querySelector('a');
                    return a ? a.href : null;
                }
                """
            )

        print(f"{text}: {href}")

    browser.close()