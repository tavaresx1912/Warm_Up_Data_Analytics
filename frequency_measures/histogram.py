import seaborn as sns
import pandas as pd

# Read the dataset
df = pd.read_csv("data.csv")

# Create a histogram plot of height data using seaborn
ax = sns.displot(
    df.Altura,  # Height column
    kde=False    # Don't show kernel density estimate
)

# Set figure size for better visualization
ax.figure.set_size_inches(10, 5)

# Set plot title and axis labels
ax.set_titles("Height Frequency Distribution", fontsize=18)
ax.set_xlabels("Meters", fontsize=14)

# Create another histogram using pandas' built-in histogram function
# with more bins for detailed visualization
df.Altura.hist(bins=50, figsize=(10, 5))