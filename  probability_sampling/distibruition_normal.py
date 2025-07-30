from scipy.stats import norm

# media = 70
# desvio_padrao = 5
#
# z = (85 - media) / desvio_padrao
#
# print(z)
#
# probabilidade = 0.8413
#
# print(norm.cdf(z))

# media = 300
# desvio_padrao = 50
#
# z_superior = (350 - media) / desvio_padrao
# z_inferior = (250 - media) / desvio_padrao
#
# probabilidade = norm.cdf(z_superior) - norm.cdf(z_inferior)
# print(probabilidade)

media = 720
desvio = 30

z_superior = (750 - media) / desvio
z_inferior = (650 - media) / desvio

probabilidade = norm.cdf(z_superior) - norm.cdf(z_inferior)

z_800 = (800 - media) / desvio
probabilidade_800 = norm.cdf(-z_800)

z_700 = (700 - media) / desvio
probabilidade_700 = norm.cdf(z_700)

print(probabilidade, probabilidade_800, probabilidade_700)
