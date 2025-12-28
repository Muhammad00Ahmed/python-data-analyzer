import pandas as pd
import matplotlib.pyplot as plt
import sys

def analyze_csv(filename):
    """Analyze CSV data and generate statistics"""
    try:
        df = pd.read_csv(filename)
        
        print("=== Data Analysis Report ===")
        print(f"\nDataset Shape: {df.shape}")
        print(f"\nColumn Names: {list(df.columns)}")
        print(f"\nData Types:\n{df.dtypes}")
        print(f"\nBasic Statistics:\n{df.describe()}")
        print(f"\nMissing Values:\n{df.isnull().sum()}")
        
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_csv(sys.argv[1])
    else:
        print("Usage: python analyze_data.py <filename.csv>")