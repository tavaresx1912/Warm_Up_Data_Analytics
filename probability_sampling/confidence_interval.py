from scipy.stats import norm

# Sample parameters
n = 50  # Sample size
sigma = 6.00  # Population standard deviation
confidence_level = 0.95  # Confidence level (95%)

# Calculate z-score for the given confidence level
# For 95% confidence, we use 0.975 (0.95 + (1-0.95)/2) for two-tailed test
z = norm.ppf(1 - (1 - confidence_level) / 2)  # For 95% confidence level, z = 1.96

# Calculate margin of error
margin_error = z * (sigma / (n ** 0.5))

# Display the result
print(f"Margin of error: R$ {margin_error:.2f}")