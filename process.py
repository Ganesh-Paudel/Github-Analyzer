import pandas as pd 

def processCommits(commitList):

    commitsDf = pd.DataFrame(commitList);

    commitsDf['date'] = pd.to_datetime(commitsDf['date']);

    commitsDf['hour'] = commitsDf['date'].dt.hour;

    commitsDf['dayOfWeek'] = commitsDf[ 'date'].dt.day_name();

    commitsDf['is_weekend'] = commitsDf['date'].dt.dayofweek > 4
    
    return commitsDf;
