import pandas as pd
import numpy as np

def clean_dataset(df):
    """Clean and preprocess the dataset."""
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Handle missing values
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    # Fill missing values for numeric columns with median
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())
    
    # Fill missing values for categorical columns with mode
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # Remove outliers using the Interquartile Range (IQR) method
    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]
    
    return df
