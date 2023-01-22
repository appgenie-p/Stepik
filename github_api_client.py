import os

import requests

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")


def get_repository_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "Authorization": f"token {GITHUB_API_TOKEN}"
    } if GITHUB_API_TOKEN else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [repo["name"] for repo in response.json()]
