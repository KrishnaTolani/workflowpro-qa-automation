import os
import uuid

from playwright.sync_api import Page, expect

from api.client import APIClient
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


BASE_URL = os.getenv(
    "BASE_URL",
    "https://app.workflowpro.com",
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://api.workflowpro.com",
)


def test_project_creation_flow(page: Page):
    """
    End-to-end integration scenario:

    1. Create project through API.
    2. Verify project through Company 1 UI.
    3. Verify Company 2 cannot see the project.

    Mobile/BrowserStack execution is described separately because
    actual BrowserStack credentials and device capabilities are
    environment-specific.
    """

    company1_token = os.getenv(
        "COMPANY1_API_TOKEN"
    )

    company2_token = os.getenv(
        "COMPANY2_API_TOKEN"
    )

    if not company1_token or not company2_token:
        raise RuntimeError(
            "API tokens must be configured in environment variables."
        )

    company1_api = APIClient(
        base_url=API_BASE_URL,
        token=company1_token,
        tenant_id="company1",
    )

    company2_api = APIClient(
        base_url=API_BASE_URL,
        token=company2_token,
        tenant_id="company2",
    )

    project_name = (
        f"Automation Project "
        f"{uuid.uuid4().hex[:8]}"
    )

    project = company1_api.create_project(
        name=project_name,
        description="Created by QA automation",
        team_members=[],
    )

    project_id = project["id"]

    try:
        # ----------------------------------------
        # 1. Verify API response
        # ----------------------------------------

        assert project["name"] == project_name
        assert project["status"] == "active"

        # ----------------------------------------
        # 2. Verify Company 1 UI
        # ----------------------------------------

        company1_email = os.getenv(
            "COMPANY1_ADMIN_EMAIL",
            "admin@company1.com",
        )

        company1_password = os.getenv(
            "COMPANY1_ADMIN_PASSWORD",
            "password123",
        )

        login_page = LoginPage(
            page,
            BASE_URL,
        )

        login_page.open()

        login_page.login(
            email=company1_email,
            password=company1_password,
        )

        login_page.verify_dashboard()

        project_page = ProjectPage(
            page,
            BASE_URL,
        )

        project_page.open()

        project_page.verify_project_visible(
            project_id=project_id,
            project_name=project_name,
        )

        # ----------------------------------------
        # 3. Tenant isolation at API level
        # ----------------------------------------

        cross_tenant_response = (
            company2_api.get_project(project_id)
        )

        assert cross_tenant_response.status_code in (
            403,
            404,
        ), (
            "Company 2 should not be able to access "
            "Company 1's project."
        )

    finally:
        # ----------------------------------------
        # 4. Cleanup
        # ----------------------------------------

        company1_api.delete_project(
            project_id
        )