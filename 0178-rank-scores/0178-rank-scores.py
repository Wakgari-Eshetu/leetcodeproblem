import pandas as pd

def order_scores(Scores: pd.DataFrame) -> pd.DataFrame:
    Scores['rank'] = Scores['score'].rank(method='dense', ascending=False).astype(int)
    result = Scores[['score', 'rank']].sort_values(by='score', ascending=False)
    return result
