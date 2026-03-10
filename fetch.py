import os
from github import Github
from dotenv import load_dotenv


load_dotenv();

class GithubFetcher:

    def __init__(self):
        self.g = Github(os.getenv("GITHUB_PTOKEN"))


    def getCommitsOfRepo(self, repoName):

        repo = self.g.get_repo(repoName);

        commits = repo.get_commits();
        commit_data = []

        for c in commits:
            commit_data.append({
                "sha": c.sha,
                "author": c.commit.author.name,
                "date": c.commit.author.date,
                "message": c.commit.message,
                "stats_additions": c.stats.additions,
                "stats_deletions": c.stats.deletions
            })
        return commit_data

    
