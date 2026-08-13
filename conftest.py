import os

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """Create one Playwright instance for the test session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright_instance: Playwright) -> Browser:
    """Launch a Chromium browser for each test."""
    browser = playwright_instance.chromium.launch(
        headless=True
    )

    yield browser

    browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    """Create an isolated browser context for each test."""
    context = browser.new_context(
        viewport={
            "width": 1280,
            "height": 800,
        }
    )

    yield context

    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()

    page.set_default_timeout(
        int(os.getenv("PLAYWRIGHT_TIMEOUT", "15000"))
    )

    yield page

    page.close()
