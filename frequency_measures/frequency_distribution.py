import pandas as pd

# Read the dataset
df = pd.read_csv("data.csv")

# Calculate maximum and minimum income values
income_max = df.Income.max()
income_min = df.Income.min()

# Define income classes and their labels
# Classes are defined by income thresholds, from lowest to highest
classes = [income_min, 1576, 3152, 7880, 15760, income_max]
labels = ['E', 'D', 'C', 'B', 'A']  # A is highest income class, E is lowest

# Calculate frequency distribution of income classes
frequency = pd.value_counts(
    pd.cut(
        x=df.Income,
        bins=classes,
        labels=labels,
        include_lowest=True
    )
)

# Calculate percentage distribution of income classes
percentage = pd.value_counts(
    pd.cut(
        x=df.Income,
        bins=classes,
        labels=labels,
        include_lowest=True
    ),
    normalize=True
)

# Create a DataFrame with frequency and percentage distributions
# Sort in descending order (from highest to lowest income class)
quantitative_freq_dist = pd.DataFrame({'Frequency': frequency, 'Percentage': percentage}).sort_index(ascending=False)

# Display the results
print(quantitative_freq_dist)