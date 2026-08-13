import os

from playwright.sync_api import Page

from pages.login_page import LoginPage


BASE_URL = os.getenv(
    "BASE_URL",
    "https://app.workflowpro.com",
)


def test_user_login(page: Page):
    """
    Validate successful user login.

    Reliability improvements:
    - Credentials are read from environment variables.
    - Page Object Model is used.
    - Playwright's retrying assertions are used.
    - No arbitrary sleep is used.
    """

    email = os.getenv(
        "COMPANY1_ADMIN_EMAIL",
        "admin@company1.com",
    )

    password = os.getenv(
        "COMPANY1_ADMIN_PASSWORD",
        "password123",
    )

    login_page = LoginPage(page, BASE_URL)

    login_page.open()

    login_page.login(
        email=email,
        password=password,
    )

    login_page.verify_dashboard()