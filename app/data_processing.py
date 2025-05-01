import pandas as pd
import streamlit as st 


def load_data(filepath):
    """Load the data from the ActivitesGarmin CSV Dataset"""
    return pd.read_csv(filepath)


def load_and_clean_data(filepath):
    """Load and clean the ActivitesGarmin dataset"""
    df = load_data(filepath)
    return df
