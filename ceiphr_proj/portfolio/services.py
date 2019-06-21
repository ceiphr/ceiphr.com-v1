import json
import requests


def get_repos():
    url = "https://api.github.com/users/ceiphr/repos"
    r = requests.get(url)
    repos = r.json()

    repo_list = []

    for i in range(len(repos)):
        repo_list.append(repos[i])

    return repo_list
