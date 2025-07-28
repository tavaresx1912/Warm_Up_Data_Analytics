import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path='data.csv'):
    """
    Loads data from a CSV file.

    Args:
        file_path: Path to the CSV file

    Returns:
        Pandas DataFrame with the loaded data
    """
    return pd.read_csv(file_path)

def calculate_statistical_measures(df, column):
    """
    Calculates quartiles, deciles, and percentiles for a specific column.

    Args:
        df: DataFrame with the data
        column: Name of the column to calculate the measures

    Returns:
        Tuple with (quartiles, deciles, percentiles)
    """
    quartiles = df[column].quantile([0.25, 0.5, 0.75])
    deciles = df[column].quantile([i / 10 for i in range(1, 10)])
    percentiles = df[column].quantile([i / 100 for i in range(1, 100)])

    return quartiles, deciles, percentiles

def create_boxplot(df, column, title, xlabel, figsize=(10, 5)):
    """
    Creates a boxplot to visualize the data distribution.

    Args:
        df: DataFrame with the data
        column: Name of the column to create the boxplot
        title: Title of the plot
        xlabel: X-axis label
        figsize: Figure size (width, height)

    Returns:
        Matplotlib axis object
    """
    plt.figure(figsize=figsize)
    ax = sns.boxplot(x=column, data=df)
    ax.set_title(title, fontsize=18)
    ax.set_xlabel(xlabel, fontsize=14)

    return ax

def main():
    # Load the data
    df = load_data()

    # Calculate statistical measures for the 'Renda' (Income) column
    quartiles, deciles, percentiles = calculate_statistical_measures(df, 'Renda')

    # Display the calculated measures
    print("Income Quartiles:")
    print(quartiles)
    print("\nIncome Deciles:")
    print(deciles)

    # Create boxplot for Height
    create_boxplot(df, 'Altura', 'Height Frequency Distribution', 'Meters')

    # Create boxplot for Income
    create_boxplot(df, 'Renda', 'Income Frequency Distribution', 'Currency')

    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()