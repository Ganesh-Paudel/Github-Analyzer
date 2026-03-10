import pandas as pd

class RepoAnalyzer:
    @staticmethod
    def calculate_activity_score(df):
       
        if df.empty: return 0
        
        daysActive = (df['date'].max() - df['date'].min()).days or 1
        commitFrequency = len(df) / daysActive
        avgImpact = df['stats_additions'].mean()
        
        score = (commitFrequency * 10) + (avgImpact * 0.1)
        return round(score, 2)

    @staticmethod
    def get_productivity_peak(df):
        """Finds the most active hour of the day."""
        df['hour'] = pd.to_datetime(df['date']).dt.hour
        return df['hour'].mode()[0]
