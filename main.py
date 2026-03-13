from re import S
from fetch import GithubFetcher
from analyze import RepoAnalyzer
import pandas as pd
import os

STORAGE = "repoCache.csv"

def run_analysis(repoName):

    df = getData(repoName)
    
    if not df.empty:
        score = RepoAnalyzer.calculate_activity_score(df)
        peakHour = RepoAnalyzer.get_productivity_peak(df)
        
        print(f"\n--- Analysis for {repoName} ---")
        print(f"Activity Score: {score}")
        print(f"Most Productive Hour: {peakHour}:00")
    else:
        print("No data found.")

def getData(repo):
    fetcher = GithubFetcher();

    newData = fetcher.getCommitsOfRepo(repo)

    if newData:
        finalDf = pd.DataFrame(newData);
        finalDf.to_csv(STORAGE, index = False)
        print(finalDf)
        return finalDf
    else:
        print("NO Commit Date")
        return pd.DataFrame()

        



if __name__ == "__main__":
    print("Welcome to Repo Analyzer,")
    print("-"*50)
    print("Repo name format = user/repoName")
    print("For eg: Ganesh-Paudel/Github-Analyzer")
    print("-"*50)
    myRepo = input("Enter the Repo Name: ")
#    myRepo = "Ganesh-Paudel/Lexical-Analysis"
    run_analysis(myRepo)
#    df = getData(myRepo);
#    print(df)

