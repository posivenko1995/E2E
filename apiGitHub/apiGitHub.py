import requests
from config import token,usernameGitHub,namerepo


url = "https://api.github.com/user/repos"
body = {"name": "{}".format(namerepo)}
response = requests.post(url, headers=token, json=body).json()
print(response)
url = "https://api.github.com/users/{}/repos".format(usernameGitHub)
response = requests.get(url, headers=token).json()
print(response)
url = "https://api.github.com/repos/{}/{}".format(usernameGitHub,namerepo)
response = requests.delete(url, headers=token)
print(response)