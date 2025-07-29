import numpy as np
from scipy.stats import poisson

# The Poisson distribution is a discrete probability distribution that expresses the probability
# of a given number of events occurring in a fixed interval of time or space, assuming these events
# occur with a known constant mean rate and independently of the time since the last event.

# Euler's number (base of natural logarithm)
e = np.e

# Parameters for the Poisson distribution
media = 20  # Lambda (λ) - average number of events in the interval
k = 25      # Number of events we want to calculate the probability for

# Manual calculation of Poisson probability mass function (PMF)
# P(X = k) = (e^(-λ) * λ^k) / k!
# probabilidade = ((e ** (-media))  * (media ** k)) / (np.math.factorial(k))

# Using scipy's poisson.pmf function to calculate the probability
# This calculates the probability of exactly k events occurring when the expected number is 'media'
probabilidade = poisson.pmf(k, media)

# Display the result - the probability of observing exactly 25 events when the average is 20
print(f"Probability of exactly {k} events occurring when the average is {media}: {probabilidade:.6f}")