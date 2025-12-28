import pandas as pd
import numpy as np
from scipy import stats

def calculate_statistics(df):
    """Calculate comprehensive statistics for the dataset"""
    
    print("=== Statistical Analysis Report ===\n")
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_columns:
        print(f"\n--- {col} ---")
        data = df[col].dropna()
        
        # Basic statistics
        print(f"Mean: {data.mean():.2f}")
        print(f"Median: {data.median():.2f}")
        print(f"Mode: {data.mode().values[0] if not data.mode().empty else 'N/A'}")
        print(f"Std Dev: {data.std():.2f}")
        print(f"Variance: {data.var():.2f}")
        
        # Range statistics
        print(f"Min: {data.min():.2f}")
        print(f"Max: {data.max():.2f}")
        print(f"Range: {data.max() - data.min():.2f}")
        
        # Quartiles
        print(f"Q1 (25%): {data.quantile(0.25):.2f}")
        print(f"Q2 (50%): {data.quantile(0.50):.2f}")
        print(f"Q3 (75%): {data.quantile(0.75):.2f}")
        print(f"IQR: {data.quantile(0.75) - data.quantile(0.25):.2f}")
        
        # Distribution tests
        skewness = stats.skew(data)
        kurtosis = stats.kurtosis(data)
        print(f"Skewness: {skewness:.2f}")
        print(f"Kurtosis: {kurtosis:.2f}")
        
        # Normality test
        if len(data) >= 8:
            statistic, p_value = stats.shapiro(data[:5000])  # Limit for performance
            print(f"Shapiro-Wilk Test p-value: {p_value:.4f}")
            print(f"Normal Distribution: {'Yes' if p_value > 0.05 else 'No'}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        df = pd.read_csv(sys.argv[1])
        calculate_statistics(df)
    else:
        print("Usage: python statistics.py <filename.csv>")