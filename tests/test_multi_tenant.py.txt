import os

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.project_page import ProjectPage


BASE_URL = os.getenv(
    "BASE_URL",
    "https://app.workflowpro.com",
)


def test_multi_tenant_access(page: Page):
    """
    Verify that a Company 2 user only sees Company 2 projects.
    """

    email = os.getenv(
        "COMPANY2_USER_EMAIL",
        "user@company2.com",
    )

    password = os.getenv(
        "COMPANY2_USER_PASSWORD",
        "password123",
    )

    login_page = LoginPage(page, BASE_URL)

    login_page.open()

    login_page.login(
        email=email,
        password=password,
    )

    login_page.verify_dashboard()

    project_page = ProjectPage(page, BASE_URL)

    project_page.open()

    projects = page.get_by_test_id("project-card")

    expect(projects.first).to_be_visible(
        timeout=15000
    )

    count = projects.count()

    assert count > 0, (
        "Expected Company 2 to have at least one project."
    )

    for index in range(count):
        project = projects.nth(index)

        expect(project).to_contain_text(
            "Company2"
        )