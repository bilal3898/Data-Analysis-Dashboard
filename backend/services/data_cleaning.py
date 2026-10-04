import pandas as pd
import numpy as np

def clean_dataset(df):
    """Clean and preprocess the dataset."""
    print(f"Starting data cleaning with {len(df)} rows and {len(df.columns)} columns")

    # Remove duplicate rows
    df = df.drop_duplicates()
    print(f"Duplicates removed: {len(df)} rows remaining")

    # Handle missing values
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    print(f"Numeric columns: {list(numeric_columns)}")
    print(f"Categorical columns: {list(categorical_columns)}")

    # Fill missing values for numeric columns with median
    for col in numeric_columns:
        if df[col].isnull().any():
            median_val = df[col].median()
            if pd.notna(median_val):
                df[col] = df[col].fillna(median_val)
                print(f"Filled {col} with median: {median_val}")
            else:
                df[col] = df[col].fillna(0)
                print(f"Filled {col} with 0 (no median available)")

    # Fill missing values for categorical columns with mode
    for col in categorical_columns:
        if df[col].isnull().any():
            try:
                mode_val = df[col].mode()[0]
                df[col] = df[col].fillna(mode_val)
                print(f"Filled {col} with mode: {mode_val}")
            except (IndexError, KeyError):
                df[col] = df[col].fillna("Unknown")
                print(f"Filled {col} with 'Unknown' (no mode available)")

    # Remove outliers using the Interquartile Range (IQR) method
    for col in numeric_columns:
        try:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            if outliers > 0:
                print(f"Removed {outliers} outliers from {col}")
            df = df[~((df[col] < lower_bound) | (df[col] > upper_bound))]
        except Exception as e:
            print(f"Could not remove outliers from {col}: {str(e)}")

    print(f"Data cleaning complete: {len(df)} rows remaining")
    return df
