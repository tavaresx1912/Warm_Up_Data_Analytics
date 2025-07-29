import pandas as pd

# This script calculates various mean values from the dataset
# and demonstrates grouping data to calculate means by category

# Read the main dataset
df = pd.read_csv("../dados.csv")

# Calculate and display the mean income for all observations
print("Mean income for all observations:")
print(df['Income'].mean())

# Calculate mean income grouped by gender
# 'Gender' column contains gender information (M = male, F = female)
mean_gender = df.groupby(['Gender'])['Income'].mean()

# Display mean income by gender
print("\nMean income by gender:")
print(mean_gender)

# Create a sample dataset for age analysis by gender
dataset = pd.DataFrame({
    'Gender': ['M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'F', 'F'],  # M = male, F = female
    'Age': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]  # Age values
})

# Calculate the overall mean age
mean = dataset['Age'].mean()

# Calculate the mean age for men only
mean_men = dataset.groupby(['Gender'])['Age'].mean().loc['M']

# Display overall mean age and mean age for men
print("\nOverall mean age and mean age for men:")
print(mean, mean_men)
