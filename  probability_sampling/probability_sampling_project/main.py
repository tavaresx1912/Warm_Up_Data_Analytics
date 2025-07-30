import pandas as pd
import numpy as np
from scipy.stats import binom, norm

# Load the dataset
df = pd.read_csv("../../dados.csv")

#---------------------------------------------------------------------------
# PROBLEM A: Probability Calculation
# Calculate the probability of selecting a group with the same proportion as the population
# (7 men and 3 women in a group of 10 individuals)
#---------------------------------------------------------------------------
k = 7  # Number of successes (men)
n = 10  # Sample size
p = 0.7  # Probability of success (proportion of men in the population)

# Calculate the probability using binomial probability mass function
probability = binom.pmf(k, n, p)
print(f"Probability of selecting a group with 7 men and 3 women: {probability:.4f}")

#---------------------------------------------------------------------------
# PROBLEM B: Sample Size Calculation
# Calculate how many groups we need to select to get 100 groups with 7 men and 3 women
#---------------------------------------------------------------------------
n_groups = 100 / probability
print(f"Number of groups needed to get 100 groups with 7 men and 3 women: {n_groups:.0f}")

#---------------------------------------------------------------------------
# PROBLEM C: Household Income Study
#---------------------------------------------------------------------------

# ITEM 1: Sample selection and parameter estimation
# Select a random sample of 200 elements and calculate mean and standard deviation
dataset = df['Renda'].sample(n=200, random_state=101)
dataset_mean = dataset.mean()
dataset_std = dataset.std()
print(f"Sample mean: {dataset_mean:.2f}")
print(f"Sample standard deviation: {dataset_std:.2f}")

# Study parameters
resource = 150000  # Available budget (R$)
interview_cost = 100  # Cost per interview (R$)

# ITEM 2: Sample size calculation for different confidence levels
# Calculate margin of error (10% of the mean)
e = 0.10 * dataset_mean

# For 90% confidence level
z = norm.ppf(0.95)  # Z-score for 90% confidence (one-tailed 0.95)
n_confidence90 = (z * dataset_std / e) ** 2
print(f"Sample size for 90% confidence level: {n_confidence90:.0f}")

# For 95% confidence level
z = norm.ppf(0.975)  # Z-score for 95% confidence (one-tailed 0.975)
n_confidence95 = (z * dataset_std / e) ** 2
print(f"Sample size for 95% confidence level: {n_confidence95:.0f}")

# For 99% confidence level
z = norm.ppf(0.995)  # Z-score for 99% confidence (one-tailed 0.995)
n_confidence99 = (z * dataset_std / e) ** 2
print(f"Sample size for 99% confidence level: {n_confidence99:.0f}")

# ITEM 3: Research cost calculation for each confidence level
cost_90 = interview_cost * n_confidence90
cost_95 = interview_cost * n_confidence95
cost_99 = interview_cost * n_confidence99
print(f"Research cost for 90% confidence level: R$ {cost_90:.2f}")
print(f"Research cost for 95% confidence level: R$ {cost_95:.2f}")
print(f"Research cost for 99% confidence level: R$ {cost_99:.2f}")

# ITEM 4: Confidence interval calculation for the highest viable confidence level
# Calculate confidence interval for 95% confidence level (assuming it's within budget)
interval = norm.interval(confidence=0.95, loc=dataset_mean, scale=dataset_std / np.sqrt(n_confidence95))
print(f"95% confidence interval: {interval}")

# ITEM 5: Margin of error calculation using all available resources
# Calculate maximum sample size with available resources
max_sample_size = resource / interview_cost
z = norm.ppf(0.975)  # Z-score for 95% confidence
# Calculate margin of error with maximum sample size
margin_error = z * (dataset_std / np.sqrt(max_sample_size))
margin_error_percent = (margin_error / dataset_mean) * 100
print(f"Maximum sample size with available resources: {max_sample_size:.0f}")
print(f"Margin of error with all resources: R$ {margin_error:.2f} ({margin_error_percent:.2f}%)")

# ITEM 6: Research cost calculation for 5% margin of error with 95% confidence level
e = 0.05 * dataset_mean  # 5% margin of error
z = norm.ppf(0.975)  # Z-score for 95% confidence
n_confidence95_5pct = (z * dataset_std / e) ** 2
cost_confidence_95_5pct = n_confidence95_5pct * interview_cost
print(f"Sample size for 95% confidence level with 5% margin of error: {n_confidence95_5pct:.0f}")
print(f"Research cost for 95% confidence level with 5% margin of error: R$ {cost_confidence_95_5pct:.2f}")