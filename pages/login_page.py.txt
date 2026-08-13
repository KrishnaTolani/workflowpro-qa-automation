from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the WorkFlow Pro login page."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(
            f"{self.base_url}/login",
            wait_until="domcontentloaded",
        )

    def login(self, email: str, password: str):
        """Login using the application's login form."""

        self.page.get_by_label("Email").fill(email)

        self.page.get_by_label("Password").fill(password)

        self.page.get_by_role(
            "button",
            name="Login",
        ).click()

    def verify_dashboard(self):
        """Verify successful navigation to dashboard."""

        expect(self.page).to_have_url(
            f"{self.base_url}/dashboard",
            timeout=15000,
        )

        expect(
            self.page.get_by_test_id("welcome-message")
        ).to_be_visible(timeout=15000)