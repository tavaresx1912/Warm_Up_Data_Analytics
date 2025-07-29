import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Descriptive Analysis of PNAD 2015 Data
# -------------------------------------------------------------------------
# This script performs a descriptive analysis of data from the National 
# Household Sample Survey (PNAD) of 2015, investigating characteristics 
# such as income, age, height, sex, and race of respondents.
# -------------------------------------------------------------------------

# Reading the dataset
df = pd.read_csv("../../dados.csv")

# -------------------------------------------------------------------------
# 1. FREQUENCY DISTRIBUTION BY INCOME CLASS
# -------------------------------------------------------------------------
# Defining income class intervals in Brazilian Reais (R$)
# Income classes:
# A ► Above 25 MW (> R$ 15,760)
# B ► From 15 to 25 MW (R$ 7,880 to R$ 15,760)
# C ► From 5 to 15 MW (R$ 3,152 to R$ 7,880)
# D ► From 2 to 5 MW (R$ 1,576 to R$ 3,152)
# E ► Up to 2 MW (< R$ 1,576)
# Considering minimum wage (MW) of R$ 788.00 at the time of the survey

income_max = df['Renda'].max()
income_min = df['Renda'].min()

# Defining class intervals in Brazilian Reais
classes = [income_min, 1576, 3152, 7880, 15760, income_max]
# Defining class labels
label = ['E', 'D', 'C', 'B', 'A']  # A is the highest income class, E is the lowest

# Building the frequency column
frequency = pd.value_counts(
    pd.cut(
        x=df['Renda'],
        bins=classes,
        labels=label,
        include_lowest=True
    )
)

# Building the percentage column
percentage = pd.value_counts(
    pd.cut(
        x=df['Renda'],
        bins=classes,
        labels=label,
        include_lowest=True
    ),
    normalize=True
)

# Joining frequency and percentage columns and sorting rows
table = pd.DataFrame({'Frequency': frequency, 'Percentage': percentage}).sort_index(ascending=False)

# Creating a bar chart to visualize the information in the table
ax = sns.barplot(x=table.index, y=table['Frequency'])
ax.set_title('Frequency Distribution by Income Class', fontsize=18)
ax.set_xlabel('Income class', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Conclusions: Based on the analyzed data, it's clear that the majority of the population is in class E,
# which demonstrates a significant concentration of people with income below 2 minimum wages.
# This highlights income inequality in Brazil, with a large portion of the population
# receiving income below or close to the minimum wage.

# -------------------------------------------------------------------------
# 2. HISTOGRAMS OF QUANTITATIVE VARIABLES
# -------------------------------------------------------------------------
# Creating histograms to visualize the distribution of quantitative variables:
# Income, Age, Height, and Income limited to R$ 20,000

# Configuring the layout with 4 charts in one row
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

# General title for all histograms
fig.suptitle('Histograms of Quantitative Variables', fontsize=16)

# --- Histogram 1: Income ---
# Visualizes the complete distribution of income in the sample
sns.histplot(data=df, x='Renda', ax=axes[0])
axes[0].set_title('Income', fontsize=14)
axes[0].set_xlabel('Income (R$)')
axes[0].set_ylabel('Count')

# --- Histogram 2: Age ---
# Visualizes the age distribution of respondents
# Using 20 bins for better visualization of the distribution
sns.histplot(data=df, x='Idade', bins=20, ax=axes[1])
axes[1].set_title('Age Distribution')
axes[1].set_xlabel('Age (years)')
axes[1].set_ylabel('Count')

# --- Histogram 3: Height ---
# Visualizes the height distribution of respondents
sns.histplot(data=df, x='Altura', ax=axes[2])
axes[2].set_title('Height Distribution')
axes[2].set_xlabel('Height (meters)')
axes[2].set_ylabel('Count')

# Adjusts the layout to ensure titles and labels don't overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# --- Histogram 4: Income up to R$ 20,000 ---
# Visualizes the income distribution limited to R$ 20,000 for better
# visualization of the distribution in the most common income range
sns.histplot(data=df.query('Renda < 20000'), x='Renda', ax=axes[3])
axes[3].set_title('Income up to R$ 20,000', fontsize=14)
axes[3].set_xlabel('Income (R$)')
axes[3].set_ylabel('Count')

# plt.show()

# Conclusions: 
# Analyzing the histograms, we can observe different distribution patterns:
# - Income: Shows a right-skewed (positive) distribution, with a concentration 
#   of lower values and a long tail to the right, indicating inequality in the distribution.
# - Age: Shows a left-skewed (negative) distribution, with a higher 
#   concentration in older ages.
# - Height: Exhibits an approximately symmetric (normal) distribution, with values 
#   concentrated around the mean.
# - Income up to R$ 20,000: Allows better visualization of the distribution for the majority of the population,
#   confirming the concentration in lower income values.

# -------------------------------------------------------------------------
# 3. ANALYSIS OF CATEGORICAL VARIABLES AND CROSS-TABULATION
# -------------------------------------------------------------------------
# Dictionaries to map numeric codes to their descriptive values

# Dictionary for the Sex variable
sex = {
    0: 'Male',
    1: 'Female'
}

# Dictionary for the Race/Color variable
race = {
    0: 'Indigenous',
    2: 'White',
    4: 'Black',
    6: 'Asian',
    8: 'Mixed',
    9: 'Not declared'
}

# Dictionary for the Years of Education variable
years_of_education = {
    1: 'No education and less than 1 year',
    2: '1 year',
    3: '2 years',
    4: '3 years',
    5: '4 years',
    6: '5 years',
    7: '6 years',
    8: '7 years',
    9: '8 years',
    10: '9 years',
    11: '10 years',
    12: '11 years',
    13: '12 years',
    14: '13 years',
    15: '14 years',
    16: '15 years or more',
    17: 'Not determined'
}

# Dictionary for the State (UF) variable
state = {
    11: 'Rondônia',
    12: 'Acre',
    13: 'Amazonas',
    14: 'Roraima',
    15: 'Pará',
    16: 'Amapá',
    17: 'Tocantins',
    21: 'Maranhão',
    22: 'Piauí',
    23: 'Ceará',
    24: 'Rio Grande do Norte',
    25: 'Paraíba',
    26: 'Pernambuco',
    27: 'Alagoas',
    28: 'Sergipe',
    29: 'Bahia',
    31: 'Minas Gerais',
    32: 'Espírito Santo',
    33: 'Rio de Janeiro',
    35: 'São Paulo',
    41: 'Paraná',
    42: 'Santa Catarina',
    43: 'Rio Grande do Sul',
    50: 'Mato Grosso do Sul',
    51: 'Mato Grosso',
    52: 'Goiás',
    53: 'Distrito Federal'
}

# Mapping codes to their descriptive values
mapped_sex = df['Sexo'].map(sex)
mapped_race = df['Cor'].map(race)

# Building a cross-tabulation between Race/Color and Sex
# This table shows the count of people for each combination of race and sex
cross_table = pd.crosstab(mapped_race, mapped_sex)

# Conclusions from the cross-tabulation:
# The cross-tabulation allows us to analyze the distribution of the population by race/color and sex.
# We can observe the representation of each group in the sample and identify
# possible differences in distribution between men and women for each racial category.

# -------------------------------------------------------------------------
# 4. DESCRIPTIVE ANALYSIS OF THE INCOME VARIABLE
# -------------------------------------------------------------------------
# Calculating measures of central tendency and dispersion for the Income variable

# Measures of central tendency
# Arithmetic mean of Income
mean_income = df['Renda'].mean()
# Median of Income (value that separates the upper half from the lower half of the data)
median_income = df['Renda'].median()
# Mode of Income (most frequent value)
mode_income = df['Renda'].mode()
# Mean absolute deviation (average of absolute differences from the mean)
mean_absolute_deviation = (df['Renda'] - df['Renda'].mean()).abs().mean()

# Dispersion measures
# Variance of Income (average of squared differences from the mean)
income_variance = df['Renda'].var()
# Standard deviation of Income (square root of variance)
income_std_dev = df['Renda'].std()

# Descriptive analysis of Income by Race and Sex
# Grouping data by Race and Sex and calculating statistics for each group
income_aggregated_table = df.groupby(['Cor', 'Sexo'])['Renda'].agg(
    mean='mean',           # Mean
    median='median',       # Median
    max='max',             # Maximum value
    mad=lambda x:(x - x.mean()).abs().mean(),  # Mean absolute deviation
    var='var',             # Variance
    std='std'              # Standard deviation
)
# Replacing codes with descriptive names in categories
income_aggregated_table.rename(index=race, level='Cor', inplace=True)
income_aggregated_table.rename(index=sex, level='Sexo', inplace=True)
print(income_aggregated_table)

# Conclusions from the descriptive analysis:
# The analysis of central tendency and dispersion measures allows us to understand
# the distribution of income in the studied population. The difference between mean and median
# indicates asymmetry in the distribution. The analysis by groups (race and sex) reveals
# disparities in income distribution among different segments of the population.

# Separatrix measures
# Quartiles of Income (divide the data into 4 equal parts)
income_quartiles = df['Renda'].quantile([0.25, 0.5, 0.75])
# Deciles of Income (divide the data into 10 equal parts)
income_deciles = df['Renda'].quantile([i / 10 for i in range(1, 10)])
# Percentiles of Income (divide the data into 100 equal parts)
income_percentiles = df['Renda'].quantile([i / 100 for i in range(1, 100)])

# -------------------------------------------------------------------------
# 5. COMPARATIVE ANALYSIS OF INCOME BY SEX AND RACE
# -------------------------------------------------------------------------
# Creating a box plot to visualize the distribution of income by sex and race

# Configuring the box plot
# Limiting the analysis to incomes below R$ 10,000 for better visualization
# Using the 'Cor' variable on the x-axis and 'Renda' on the y-axis
# Adding 'Sexo' as a third variable through the 'hue' parameter
ax = sns.boxplot(
    x = 'Cor',
    y = 'Renda',
    hue = 'Sexo',
    data = df.query('Renda < 10000'),  # Filtering incomes below R$ 10,000
    # Ordering race categories alphabetically and excluding 'Not declared'
    order = [k for k, v in sorted(race.items(), key=lambda item: item[1]) if k != 9],
    hue_order = [0, 1]  # Order for the legend: Male, Female
)

# Configuring x-axis labels with race names
ax.set_xticklabels(
    [race[k] for k, v in sorted(race.items(), key=lambda item: item[1]) if k != 9], 
    rotation=45,  # Rotating labels for better visualization
    horizontalalignment='right'
)

# Configuring the legend
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, [sex[0], sex[1]], title='Sex')

# Configuring the chart title
ax.set_title('Box Plot of Income by Sex and Race (Income < R$ 10,000)', fontsize=18)

# Conclusions from the box plot:
# The box plot allows us to visualize and compare the income distribution among different
# groups of sex and race. We can observe:
# - Differences in median income between men and women within each racial category
# - Variations in income dispersion (box size) among groups
# - Presence of outliers (extreme values) in some groups
# - Patterns of income inequality that may be related to both sex and race
# This visualization complements the previous statistical analysis, allowing a
# more intuitive interpretation of income disparities.

# Show the chart
plt.show()