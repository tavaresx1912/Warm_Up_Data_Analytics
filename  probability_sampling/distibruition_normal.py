from scipy.stats import norm

# Example 1 (commented out)
# mean = 70
# standard_deviation = 5
#
# z = (85 - mean) / standard_deviation
#
# print(z)
#
# probability = 0.8413
#
# print(norm.cdf(z))

# Example 2 (commented out)
# mean = 300
# standard_deviation = 50
#
# z_upper = (350 - mean) / standard_deviation
# z_lower = (250 - mean) / standard_deviation
#
# probability = norm.cdf(z_upper) - norm.cdf(z_lower)
# print(probability)

# Example 3 (active)
mean = 720
standard_deviation = 30

# Calculate probability between 650 and 750
z_upper = (750 - mean) / standard_deviation
z_lower = (650 - mean) / standard_deviation
probability_between = norm.cdf(z_upper) - norm.cdf(z_lower)

# Calculate probability of being greater than 800
z_800 = (800 - mean) / standard_deviation
probability_greater_than_800 = norm.cdf(-z_800)

# Calculate probability of being less than 700
z_700 = (700 - mean) / standard_deviation
probability_less_than_700 = norm.cdf(z_700)

# Display results
print(f"Probability between 650 and 750: {probability_between:.4f}")
print(f"Probability greater than 800: {probability_greater_than_800:.4f}")
print(f"Probability less than 700: {probability_less_than_700:.4f}")