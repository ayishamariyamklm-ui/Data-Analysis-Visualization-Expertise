"""
Utility Functions Module
Reusable helper functions for data analysis
"""

import pandas as pd


def dataset_overview(df):
    """
    Print dataset overview
    """
    print("Dataset Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())


def missing_values_report(df):
    """
    Generate missing values report
    """
    missing = df.isnull().sum()

    report = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    return report


def save_dataframe(df, filepath):
    """
    Save dataframe to CSV
    """
    df.to_csv(filepath, index=False)


def print_section(title):
    """
    Print formatted section title
    """
    print("\n" + "="*50)
    print(title)
    print("="*50)