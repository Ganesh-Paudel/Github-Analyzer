from fetch import GithubFetcher
from process import processCommits 

def run():

    fetchIt = GithubFetcher()
    commits = fetchIt.getCommitsOfRepo("Ganesh-Paudel/Github-Analyzer")
    commitsData = processCommits(commits)
    print(commitsData)


if __name__ == "__main__":
    run()
