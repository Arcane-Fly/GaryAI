import os
import getpass
import requests
import subprocess

def check_repo_exists(user, repo_name):
    url = f"https://api.github.com/repos/{user}/{repo_name}"
    response = requests.get(url)
    return response.status_code == 200

def create_repo(user, password, repo_name):
    url = f"https://api.github.com/user/repos"
    payload = {"name": repo_name, "private": True}
    response = requests.post(url, auth=(user, password), json=payload)
    return response.status_code == 201

def clone_repo(user, repo_name):
    url = f"https://github.com/{user}/{repo_name}.git"
    subprocess.run(["git", "clone", url])

def commit_push_changes(user, password, repo_name):
    os.chdir(repo_name)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "auto commit"])
    subprocess.run(["git", "push", "origin", "master"])

def main():
    user = getpass.getuser()
    password = getpass.getpass()
    repo_name = "GaryAI"

    if not check_repo_exists(user, repo_name):
        if create_repo(user, password, repo_name):
            print(f"Created repository {repo_name}")
        else:
            print(f"Failed to create repository {repo_name}")
            return

    clone_repo(user, repo_name)
    # Make changes to the repo
    commit_push_changes(user, password, repo_name)

if __name__ == "__main__":
    main()
