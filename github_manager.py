from github import Github

class GithubManager:
    def __init__(self, token):
        self.github = Github(token)

    def create_or_get_repo(self, repo_name):
        # Check if the repo exists, if not create it
        # Return the repo

    def get_code_from_repo(self, repo_name):
        # Get the code from the repo
        # Return the code

    def update_repo(self, repo, code):
        # Update the repo with the given code
