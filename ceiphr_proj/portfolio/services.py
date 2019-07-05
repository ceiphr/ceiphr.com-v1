import os
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


def get_shots():
    url = "https://api.dribbble.com/v2/user/shots?access_token=%s" % os.getenv("DRIBBBLE_ACCESS_TOKEN", default="")
    r = requests.get(url)
    shots = r.json()

    shot_list = []

    for i in range(len(shots)):
        shot_list.append(shots[i])

    return shot_list
