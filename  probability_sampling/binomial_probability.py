from scipy.special import comb
from scipy.stats import binom

# # Defining parameters for a coin toss example
# n = 4  # number of tosses
# k = 2  # number of desired successes (heads)
# p = 0.5  # probability of success in each toss (fair coin)
#
#
# # Calculating the probability using binomial distribution
# probabilidade = binom.pmf(k, n, p)
#
# # Displaying the result
# print(f"Probability of getting exactly {k} heads in {n} tosses: {probabilidade:.4f}")


# Defining parameters for a dice roll example
n = 10  # total number of rolls
k = 3   # minimum number of successes
p = 1 / 6  # probability of rolling a 5

# Calculating the probability of getting k or more successes
# We use 1 - CDF(k-1) to find P(X ≥ k)
probabilidade = 1 - binom.cdf(k - 1, n, p)

print(f"Probability of rolling a 5 at least {k} times in {n} rolls: {probabilidade:.4f}")