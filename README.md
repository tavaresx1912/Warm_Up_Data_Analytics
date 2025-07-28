# Data Analytics Warm-Up Project

This repository contains a collection of Python scripts for basic data analysis and visualization, focusing on frequency distributions and histograms.

## Project Structure

- **frequency_measures/** - Directory containing scripts for frequency analysis
  - **data.csv** - Dataset containing demographic information (UF, Gender, Age, Race, Years of Education, Income, Height)
  - **frequency_distribution.py** - Script to calculate and display frequency and percentage distributions of income by class
  - **histogram.py** - Script to create histograms of height data using both seaborn and pandas
  - **mean.py** - Script to calculate various mean values from the dataset
  - **median_mode.py** - Script to calculate and display the median and mode of income data
  - **quartiles.py** - Script to calculate quartiles, deciles, and percentiles and create boxplots
  - **sturges_rule.py** - Script to calculate optimal bin count using Sturges' rule and create frequency distributions

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

## Data Description

The dataset contains the following columns:
- UF - State or region code
- Sexo - Gender
- Idade - Age
- Cor - Race/Color
- Anos de Estudo - Years of Education
- Renda - Income
- Altura - Height