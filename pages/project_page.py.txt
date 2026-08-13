from playwright.sync_api import Page, expect


class ProjectPage:
    """Page Object for project-related UI operations."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(
            f"{self.base_url}/projects",
            wait_until="domcontentloaded",
        )

    def verify_project_visible(
        self,
        project_id: int,
        project_name: str,
    ):
        project = self.page.get_by_test_id(
            f"project-{project_id}"
        )

        expect(project).to_be_visible(
            timeout=30000
        )

        expect(project).to_contain_text(
            project_name
        )

    def verify_project_not_visible(
        self,
        project_id: int,
    ):
        project = self.page.get_by_test_id(
            f"project-{project_id}"
        )

        expect(project).to_have_count(0)