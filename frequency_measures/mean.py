import pandas as pd

# This script calculates various mean values from the dataset
# and demonstrates grouping data to calculate means by category

# Read the main dataset
df = pd.read_csv("data.csv")

# Calculate and display the mean income for all observations
print("Mean income for all observations:")
print(df['Renda'].mean())

# Calculate mean income grouped by gender
# 'Sexo' column contains gender information (H = male, M = female)
mean_sexo = df.groupby(['Sexo'])['Renda'].mean()

# Display mean income by gender
print("\nMean income by gender:")
print(mean_sexo)

# Create a sample dataset for age analysis by gender
dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],  # H = male, M = female
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]  # Age values
})

# Calculate the overall mean age
mean = dataset['Idade'].mean()

# Calculate the mean age for men only
mean_men = dataset.groupby(['Sexo'])['Idade'].mean().loc['H']

# Display overall mean age and mean age for men
print("\nOverall mean age and mean age for men:")
print(mean, mean_men)
