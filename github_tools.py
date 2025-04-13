import requests
from pydantic import BaseModel
from pydantic_ai import Tool


class RepoInput(BaseModel):
    owner: str
    repo: str


@Tool
def get_repo_summary(data: RepoInput) -> str:
    """
        Fetches and summarizes metadata for a given public GitHub repository

        Args:
            data:   RepoInput model

        Returns:
            String with summary of response metadata
    """
    url = f"https://api.github.com/repos/{data.owner}/{data.repo}"

    response: requests.Response = requests.get(url, timeout=10)
    if response.status_code != 200:
        return f'Failed to fetch repo: {response.status_code} - {response.text}'

    repo_info = response.json()
    # print(json.dumps(repo_info, indent=4))
    return (
        f"Repo: {repo_info['full_name']}\n"
        f"Description: {repo_info['description']}\n"
        f"Stars: {repo_info['stargazers_count']}, Forks: {repo_info['forks_count']}, "
        f"Open Issues: {repo_info['open_issues_count']}\n"
        f"Default Branch: {repo_info['default_branch']}"
    )
