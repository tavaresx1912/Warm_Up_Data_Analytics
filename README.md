# Data Analytics Warm-Up Project

This repository contains a collection of Python scripts for basic data analysis and visualization, focusing on frequency distributions and histograms.

## Project Structure

- **frequency_measures/** - Directory containing scripts for frequency analysis
  - **data.csv** - Dataset containing demographic information (UF, Gender, Age, Race, Years of Education, Income, Height)
  - **frequency_distribution.py** - Script to calculate and display frequency and percentage distributions of income by class
  - **histogram.py** - Script to create histograms of height data using both seaborn and pandas
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
```

## Description of Scripts

### frequency_distribution.py

This script categorizes income data into 5 classes (A through E, with A being the highest income class) and calculates the frequency and percentage distribution for each class.

### histogram.py

This script creates visualizations of height data using both seaborn's displot and pandas' built-in histogram function.

### sturges_rule.py

This script implements Sturges' rule to calculate the optimal number of bins for a histogram based on the number of observations. It then creates frequency and percentage distributions for income data.

## Data Description

The dataset contains the following columns:
- UF - State or region code
- Sexo - Gender
- Idade - Age
- Cor - Race/Color
- Anos de Estudo - Years of Education
- Renda - Income
- Altura - Height