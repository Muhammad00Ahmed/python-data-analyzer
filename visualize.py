import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    """Create various visualizations for the dataset"""
    
    # Set style
    sns.set_style("whitegrid")
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Histogram
    df.hist(ax=axes[0, 0])
    axes[0, 0].set_title('Data Distribution')
    
    # Correlation heatmap
    if df.select_dtypes(include=['number']).shape[1] > 1:
        sns.heatmap(df.corr(), annot=True, ax=axes[0, 1], cmap='coolwarm')
        axes[0, 1].set_title('Correlation Matrix')
    
    # Box plot
    df.boxplot(ax=axes[1, 0])
    axes[1, 0].set_title('Box Plot')
    
    # Line plot
    df.plot(ax=axes[1, 1])
    axes[1, 1].set_title('Line Plot')
    
    plt.tight_layout()
    plt.savefig('visualizations.png')
    print("Visualizations saved to visualizations.png")
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    import sys
    
    if len(sys.argv) > 1:
        df = pd.read_csv(sys.argv[1])
        create_visualizations(df)
    else:
        print("Usage: python visualize.py <filename.csv>")