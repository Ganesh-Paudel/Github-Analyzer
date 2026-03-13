import pandas as pd

class RepoAnalyzer:
    @staticmethod
    def calculate_activity_score(df):

        if df.empty:
            return

        commitReward = 10
        codeChangeReward = 5
        mulDayReward = 2 
        
        totalCommits = len(df)

        totalLinesChanged = df['additions'].sum() + df['deletions'].sum()
        averageImpactPerCommit = totalLinesChanged / totalCommits

        df['date'] = pd.to_datetime(df['date'])
        uniqueDays = df['date'].dt.date.nunique()

        score = (totalCommits * commitReward) + (averageImpactPerCommit * codeChangeReward) + (uniqueDays * mulDayReward)
        return score;

    @staticmethod
    def get_productivity_peak(df):
        df['hour'] = pd.to_datetime(df['date']).dt.hour
        return df['hour'].mode()[0]
