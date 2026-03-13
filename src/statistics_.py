"""
Statistical Analysis Module
Provides statistical summaries and calculations
"""

import pandas as pd


def descriptive_statistics(df):
    """
    Generate descriptive statistics
    """
    return df.describe()


def calculate_mean(df, column):
    """
    Calculate mean value
    """
    return df[column].mean()


def calculate_median(df, column):
    """
    Calculate median value
    """
    return df[column].median()


def calculate_std(df, column):
    """
    Calculate standard deviation
    """
    return df[column].std()


def correlation_matrix(df):
    """
    Generate correlation matrix
    """
    return df.corr(numeric_only=True)


def calculate_percentage(part, whole):
    """
    Calculate percentage
    """
    if whole == 0:
        return 0

    return (part / whole) * 100