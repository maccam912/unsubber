from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Browser, Page, Playwright


class Session:
    playwright: Playwright
    browser: Browser
    page: Page

    def __init__(self, url: str):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.page.goto(url)

    def exit(self) -> None:
        self.browser.close()
        self.playwright.stop()

    def get_content(self) -> str:
        return self.page.content()
