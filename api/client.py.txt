import requests


class APIClient:
    """Simple API client for WorkFlow Pro."""

    def __init__(
        self,
        base_url: str,
        token: str,
        tenant_id: str,
    ):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "X-Tenant-ID": tenant_id,
                "Content-Type": "application/json",
            }
        )

    def create_project(
        self,
        name: str,
        description: str,
        team_members: list,
    ):
        response = self.session.post(
            f"{self.base_url}/api/v1/projects",
            json={
                "name": name,
                "description": description,
                "team_members": team_members,
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_project(self, project_id: int):
        return self.session.get(
            f"{self.base_url}/api/v1/projects/{project_id}",
            timeout=10,
        )

    def delete_project(self, project_id: int):
        return self.session.delete(
            f"{self.base_url}/api/v1/projects/{project_id}",
            timeout=10,
        )