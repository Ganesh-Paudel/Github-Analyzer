import os
import time
from github import Github, GithubException
from dotenv import load_dotenv


load_dotenv();

class GithubFetcher:

    def __init__(self):
        self.g = Github(os.getenv("GITHUB_PTOKEN"))


    def getCommitsOfRepo(self, repoName):

        try:

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
        except GithubException as e:
            print("Error fetching data: ", e)
            return []


    def checkRateLimit(self):
        limits = self.g.get_rate_limit();
        remainingTime = limits.core.remainingTime;
        resetTime = limits.core.resetTime;
        print(f"API Status: {remainingTime} requests left.")

        if remainingTime < 10:
            sleepTime = (resetTime - time.time()) + 5;
            print(f"Low Rate Limit: Sleeping for {sleepTime}")
            time.sleep(max(0,sleepTime))

    
