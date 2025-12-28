import pandas as pd
import numpy as np

def clean_data(df):
    """Clean and preprocess data"""
    
    print("=== Data Cleaning Report ===\n")
    
    # Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows")
    
    # Handle missing values
    missing_before = df.isnull().sum().sum()
    
    # Fill numeric columns with median
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    
    # Fill categorical columns with mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')
    
    missing_after = df.isnull().sum().sum()
    print(f"Filled {missing_before - missing_after} missing values")
    
    # Remove outliers using IQR method
    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    print(f"\nFinal dataset shape: {df.shape}")
    
    return df

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        df = pd.read_csv(sys.argv[1])
        cleaned_df = clean_data(df)
        output_file = sys.argv[1].replace('.csv', '_cleaned.csv')
        cleaned_df.to_csv(output_file, index=False)
        print(f"\nCleaned data saved to {output_file}")
    else:
        print("Usage: python clean_data.py <filename.csv>")