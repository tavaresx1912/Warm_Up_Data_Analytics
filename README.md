# Data Analytics Warm-Up Project

This repository contains a collection of Python scripts for basic data analysis and visualization, focusing on frequency distributions, histograms, and descriptive statistics.

## Project Structure

- **frequency_measures/** - Directory containing scripts for frequency analysis
  - **data.csv** - Dataset containing demographic information (UF, Gender, Age, Race, Years of Education, Income, Height)
  - **frequency_distribution.py** - Script to calculate and display frequency and percentage distributions of income by class
  - **histogram.py** - Script to create histograms of height data using both seaborn and pandas
  - **mean.py** - Script to calculate various mean values from the dataset
  - **median_mode.py** - Script to calculate and display the median and mode of income data
  - **quartiles.py** - Script to calculate quartiles, deciles, and percentiles and create boxplots
  - **standard_deviation.py** - Script to calculate mean absolute deviation, variance, and standard deviation
  - **sturges_rule.py** - Script to calculate optimal bin count using Sturges' rule and create frequency distributions
  - **descriptive_analysis_project/** - Comprehensive descriptive analysis project using PNAD 2015 data
    - **dados.csv** - Dataset from the National Household Sample Survey (PNAD) 2015
    - **main.py** - Script performing a complete descriptive analysis of demographic and socioeconomic data
    - **Análise_Descritiva.ipynb** - Jupyter notebook with instructions and guidelines for the analysis
- **probability_sampling/** - Directory containing scripts for probability distributions and sampling
  - **binomial_probability.py** - Script to calculate binomial probabilities for dice rolls and coin tosses
  - **poisson.py** - Script to calculate Poisson probabilities for event occurrences
  - **normal_distribution.py** - Script to calculate normal distribution probabilities for various scenarios
  - **confidence_interval.py** - Script to calculate confidence intervals for population parameters

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib (dependency for seaborn)

## Usage

Each script can be run independently:

```bash
# To run the frequency distribution analysis
python frequency_measures/frequency_distribution.py

# To generate histograms of height data
python frequency_measures/histogram.py

# To calculate optimal bin count using Sturges' rule
python frequency_measures/sturges_rule.py

# To calculate and display mean values
python frequency_measures/mean.py

# To calculate and display median and mode values
python frequency_measures/median_mode.py

# To calculate quartiles, deciles, percentiles and create boxplots
python frequency_measures/quartiles.py

# To calculate mean absolute deviation, variance, and standard deviation
python frequency_measures/standard_deviation.py

# To run the comprehensive descriptive analysis project
python frequency_measures/descriptive_analysis_project/main.py

# To calculate binomial probabilities
python probability_sampling/binomial_probability.py

# To calculate Poisson probabilities
python probability_sampling/poisson.py

# To calculate normal distribution probabilities
python probability_sampling/normal_distribution.py

# To calculate confidence intervals
python probability_sampling/confidence_interval.py
```

## Description of Scripts

### frequency_distribution.py

This script categorizes income data into 5 classes (A through E, with A being the highest income class) and calculates the frequency and percentage distribution for each class.

### histogram.py

This script creates visualizations of height data using both seaborn's displot and pandas' built-in histogram function.

### sturges_rule.py

This script implements Sturges' rule to calculate the optimal number of bins for a histogram based on the number of observations. It then creates frequency and percentage distributions for income data.

### mean.py

This script calculates various mean values from the dataset and demonstrates grouping data to calculate means by category. It calculates the overall mean income, mean income by gender, and also works with a sample dataset to calculate mean age overall and mean age for men.

### median_mode.py

This script calculates and displays the median and mode of income data. The median represents the middle value when data is sorted, while the mode represents the most frequently occurring value in the dataset.

### quartiles.py

This script calculates statistical measures (quartiles, deciles, and percentiles) and creates boxplot visualizations. It includes functions for:
- Loading data from a CSV file
- Calculating quartiles (25th, 50th, and 75th percentiles), deciles (10th through 90th percentiles), and percentiles (1st through 99th percentiles) for a specified column
- Creating boxplots to visualize the distribution of data
- Displaying the calculated statistical measures

The script demonstrates these capabilities by calculating quartiles and deciles for income data and creating boxplots for both height and income distributions.

### standard_deviation.py

This script calculates various measures of dispersion including mean absolute deviation, variance, and standard deviation. It demonstrates:
- Calculating mean absolute deviation for income data
- Working with a sample dataset of student grades to calculate and compare dispersion measures
- Calculating variance and standard deviation for different datasets
- Filtering data by gender to calculate standard deviation for specific groups

The script provides examples of how these statistical measures can be used to understand the spread or variability in different types of data.

### descriptive_analysis_project/main.py

This script performs a comprehensive descriptive analysis of data from the National Household Sample Survey (PNAD) 2015, investigating demographic and socioeconomic characteristics. The analysis is divided into five main sections:

1. **Frequency Distribution by Income Class** - Categorizes income data into 5 classes (A through E) based on minimum wage multiples and analyzes the distribution across these classes.

2. **Histograms of Quantitative Variables** - Creates and analyzes histograms for income, age, height, and income limited to R$ 20,000 to visualize their distributions and identify patterns.

3. **Analysis of Categorical Variables and Cross-Tabulation** - Uses dictionaries to map numeric codes to descriptive values for sex, race/color, education years, and states, then creates cross-tabulations to analyze relationships between categorical variables.

4. **Descriptive Analysis of the Income Variable** - Calculates various statistical measures for income data:
   - Measures of central tendency (mean, median, mode)
   - Measures of dispersion (mean absolute deviation, variance, standard deviation)
   - Separatrix measures (quartiles, deciles, percentiles)
   - Grouped analysis by race and sex

5. **Comparative Analysis of Income by Sex and Race** - Creates box plots to visualize and compare income distribution across different demographic groups, highlighting disparities and patterns.

The script includes detailed comments explaining the methodology and conclusions drawn from each analysis, making it a comprehensive example of descriptive statistical analysis applied to real-world socioeconomic data.

### normal_distribution.py

This script demonstrates the application of the normal distribution to calculate probabilities for various scenarios. It uses the scipy.stats.norm module to:

- Calculate the probability of a value falling within a specific range (between 650 and 750)
- Calculate the probability of a value being greater than a threshold (greater than 800)
- Calculate the probability of a value being less than a threshold (less than 700)

The script includes examples with standardized z-scores and shows how to interpret normal distribution probabilities in practical scenarios. It's useful for understanding how the normal distribution applies to real-world data analysis problems.

### confidence_interval.py

This script demonstrates how to calculate confidence intervals for population parameters based on sample statistics. It covers:

- Calculating confidence intervals for population means
- Working with different confidence levels (e.g., 95%, 99%)
- Interpreting the margin of error
- Applying confidence intervals to real-world sampling problems

The script provides practical examples of how confidence intervals help quantify the uncertainty in statistical estimates and support decision-making based on sample data.

## Data Description

The dataset contains the following columns:
- UF - State or region code
- Gender - Male (M) or Female (F)
- Age - Age in years
- Race - Race/ethnicity code
- Years_of_Education - Number of years of formal education
- Income - Income in currency units
- Height - Height in meters

The PNAD 2015 dataset (dados.csv) contains similar variables but with more detailed categorizations and is focused on data from the Brazilian National Household Sample Survey.