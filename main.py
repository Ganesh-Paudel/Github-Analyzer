from fetch import GithubFetcher
from analyze import RepoAnalyzer
import pandas as pd

def run_analysis(repoName):
    fetcher = GithubFetcher()
    print(f"Fetching data for {repoName}...")
    
    rawData = fetcher.getCommitsOfRepo(repoName)
    df = pd.DataFrame(rawData)
    
    if not df.empty:
        score = RepoAnalyzer.calculate_activity_score(df)
        peakHour = RepoAnalyzer.get_productivity_peak(df)
        
        print(f"\n--- Analysis for {repoName} ---")
        print(f"Activity Score: {score}")
        print(f"Most Productive Hour: {peakHour}:00")
    else:
        print("No data found.")

if __name__ == "__main__":
    myRepo = "Ganesh-Paudel/Lexical-Analysis"
    run_analysis(myRepo)
