"""
Visualization Module
Contains reusable visualization functions
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_histogram(df, column):
    """
    Plot histogram for a column
    """
    plt.figure(figsize=(8,5))
    plt.hist(df[column], bins=20)

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.show()


def plot_line(df, column):
    """
    Plot line chart for a column
    """
    plt.figure(figsize=(10,5))

    plt.plot(df[column])

    plt.title(f"{column} Trend")
    plt.xlabel("Index")
    plt.ylabel(column)

    plt.show()


def plot_scatter(df, x, y):
    """
    Scatter plot between two variables
    """
    plt.figure(figsize=(8,5))

    plt.scatter(df[x], df[y])

    plt.title(f"{x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)

    plt.show()


def correlation_heatmap(df):
    """
    Plot correlation heatmap
    """
    corr = df.corr(numeric_only=True)

    plt.figure(figsize=(10,6))
    sns.heatmap(corr, annot=True)

    plt.title("Correlation Matrix")

    plt.show()