"""
Data Cleaning Module
Handles dataset preprocessing and preparation
"""

import pandas as pd


def load_data(filepath):
    """
    Load dataset from CSV file
    """
    df = pd.read_csv(filepath)
    return df


def check_missing_values(df):
    """
    Check missing values in dataset
    """
    return df.isnull().sum()


def remove_duplicates(df):
    """
    Remove duplicate rows
    """
    return df.drop_duplicates()


def handle_missing_values(df, method="drop"):
    """
    Handle missing values
    """
    if method == "drop":
        df = df.dropna()

    elif method == "fill_mean":
        df = df.fillna(df.mean(numeric_only=True))

    elif method == "fill_median":
        df = df.fillna(df.median(numeric_only=True))

    return df


def convert_to_datetime(df, column):
    """
    Convert column to datetime format
    """
    df[column] = pd.to_datetime(df[column])
    return df


def clean_dataset(filepath):
    """
    Complete cleaning pipeline
    """
    df = load_data(filepath)

    df = remove_duplicates(df)
    df = handle_missing_values(df)

    return df