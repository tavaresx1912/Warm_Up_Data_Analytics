from scipy.stats import norm

# Sample size
n = 50
# Population standard deviation
sigma = 6.00
# Confidence level 95% (z = 1.96)
z = norm.ppf(0.975)  # For 95% confidence level

# Calculate margin of error
margin_error = z * (sigma / (n ** 0.5))

print(f"Margin of error: R$ {margin_error:.2f}")
