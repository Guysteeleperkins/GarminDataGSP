import pandas as pd


def load_data(filepath):
    """Load the data from the ActivitesGarmin CSV Dataset"""
    return pd.read_csv(filepath)


def load_and_clean_data(filepath):
    """Load and clean the ActivitesGarmin dataset"""
    df = load_data(filepath)
    df = drop_unnecessary_columns(df)
    return df


def drop_unnecessary_columns(df):
    """Drop any unnecessary columns and duplicates"""
    df.drop(columns=["Favorite",
                     "Avg Bike Cadence",
                     "Max Bike Cadence",
                     "Total Strokes",
                     "Avg. Swolf",
                     "Avg Stroke Rate",
                     "Decompression",
                     "Normalized Power® (NP®)",
                     "Total Runs",
                     "Longest Run",
                     "Max Speed",
                     "Active Time",
                     "Total Run Distance",
                     "Avg Run Speed"],
            inplace=True)
    df.drop_duplicates(inplace=True)
    return df
