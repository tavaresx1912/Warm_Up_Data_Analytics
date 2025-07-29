import pandas as pd

# This script calculates and displays the median and mode of income data

# Read the dataset
df = pd.read_csv('../dados.csv')

# Calculate and display the median income
# The median is the middle value when data is sorted
print("Median income:")
print(df['Income'].median())

# Calculate and display the mode of income
# The mode is the most frequently occurring value
print("\nMode income (most frequent value):")
print(df['Income'].mode())

