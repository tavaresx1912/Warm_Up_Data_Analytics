import numpy as np
import pandas as pd

# Read the dataset
df = pd.read_csv("data.csv")

# Get the number of observations
n = df.shape[0]

# Calculate the optimal number of bins using Sturges' rule
# Formula: k = 1 + (10/3) * log10(n)
k = int(round(1 + (10 / 3) * np.log10(n), 0))
print(f"Optimal number of bins according to Sturges' rule: {k}")

# Calculate frequency distribution of income using the calculated number of bins
frequency = pd.value_counts(
    pd.cut(
        x=df.Income,
        bins=17,  # Using 17 bins (could be replaced with k for dynamic binning)
        include_lowest=True
    ),
    sort=False
)

# Calculate percentage distribution of income
percentage = pd.value_counts(
    pd.cut(
        x=df.Income,
        bins=17,  # Using 17 bins (could be replaced with k for dynamic binning)
        include_lowest=True
    ),
    sort=False,
    normalize=True
)

# Create a DataFrame with frequency and percentage distributions
# Fixed the bug: added parentheses to sort_index method
quantitative_freq_dist = pd.DataFrame({'Frequency': frequency, 'Percentage': percentage}).sort_index()
print(quantitative_freq_dist)