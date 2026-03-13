# Data Validation

## Overview

Data validation ensures datasets are accurate, consistent, and suitable for analysis. Validation processes are performed before conducting exploratory analysis.

---

# 1. Missing Value Detection

Missing values can affect analysis accuracy.

Example:

```python
df.isnull().sum()

Handling methods:

Fill with mean or median
Forward or backward fill
Remove rows if necessary

Example:

df.fillna(df.mean(), inplace=True)


# 2. Duplicate Record Detection

Duplicate entries can lead to incorrect analysis.

Check duplicates:

df.duplicated().sum()

Remove duplicates:

df.drop_duplicates(inplace=True)


# 3. Data Type Validation

Ensures each column has the correct data type.

Example check:

df.dtypes

Example correction:

df['date'] = pd.to_datetime(df['date'])

# 4. Outlier Detection

Outliers can significantly impact statistical results.

Methods used:

Boxplot visualization
Statistical thresholds

Example:

sns.boxplot(data=df)

# 5. Range Validation

Ensures values fall within logical limits.

Examples:

Dataset	Valid Range
Student scores	0 – 100
Temperature	realistic weather range
Stock prices	positive values
COVID cases	non-negative integers

Example validation:

df = df[df['score'] <= 100]

# 6. Consistency Checks

Checks logical relationships within data.

Example:

Active cases calculation:
Active Cases = Confirmed − Recovered − Deaths

Implementation:

df['active_cases'] = df['confirmed'] - df['recovered'] - df['deaths']

# 7. Final Data Quality Checks

Final verification before analysis includes:

Dataset shape verification
Data type checks
Null value verification
Column consistency

Example:

print(df.shape)
print(df.info())

# Conclusion

Data validation ensures the accuracy, reliability, and integrity of the datasets used in this portfolio.
