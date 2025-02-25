"""
Data Collection Script for Middle-Income Countries Policy Analysis

This script collects World Bank Development Indicators data for middle-income
countries, focusing on economic policies and growth indicators from 2000-2020.
"""

import os
import pandas as pd
import numpy as np
import wbdata
import matplotlib.pyplot as plt
from datetime import datetime
import time

# Create data directories if they don't exist
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

print("Collecting data from World Bank Development Indicators...")

# 1. Get list of middle-income countries
print("Fetching middle-income country list...")
lmic = [c['id'] for c in wbdata.get_country(incomelevel="LMC", display=False)]
umic = [c['id'] for c in wbdata.get_country(incomelevel="UMC", display=False)]
middle_income = lmic + umic

# Save country list for reference
country_info = []
for c in wbdata.get_country():
    if c['id'] in middle_income:
        income_level = "LMIC" if c['id'] in lmic else "UMIC"
        country_info.append({
            'id': c['id'],
            'name': c['name'],
            'income_level': income_level,
            'region': c.get('region', {}).get('value', '')
        })

country_df = pd.DataFrame(country_info)
country_df.to_csv('data/raw/middle_income_countries.csv', index=False)
print(f"Identified {len(middle_income)} middle-income countries.")

# 2. Define required indicators
indicators = {
    # Economic indicators
    "NY.GDP.PCAP.CD": "gdp_per_capita",           # GDP per capita (current US$)
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",            # GDP growth (annual %)
    
    # Policy variables
    "SE.XPD.TOTL.GD.ZS": "education_exp",         # Gov expenditure on education (% of GDP)
    "SH.XPD.CHEX.GD.ZS": "health_exp",            # Current health expenditure (% of GDP)
    "NE.GDI.TOTL.ZS": "investment",               # Gross capital formation (% of GDP)
    "GB.XPD.RSDV.GD.ZS": "rd_exp",                # R&D expenditure (% of GDP)
    "NE.TRD.GNFS.ZS": "trade_openness",           # Trade (% of GDP)
    "GC.XPN.TOTL.GD.ZS": "govt_expenditure",      # Government expenditure (% of GDP)
    
    # Infrastructure indicators
    "IT.NET.USER.ZS": "internet_users",           # Individuals using the Internet (% of population)
    "EG.ELC.ACCS.ZS": "electricity_access",       # Access to electricity (% of population)
    
    # Human capital indicators
    "SE.SEC.ENRR": "secondary_enrollment",        # School enrollment, secondary (% gross)
    "SE.TER.ENRR": "tertiary_enrollment",         # School enrollment, tertiary (% gross)
}

# 3. Set time range
dates = (datetime(2000, 1, 1), datetime(2020, 1, 1))

# 4. Get data with error handling and rate limiting
print(f"Fetching data for {len(indicators)} indicators...")
all_data = []

for i, (indicator_code, indicator_name) in enumerate(indicators.items()):
    try:
        print(f"Fetching {indicator_name} ({i+1}/{len(indicators)})...")
        
        # Get data for this indicator
        data = wbdata.get_data(indicator_code, country=middle_income, data_date=dates)
        
        # Convert to DataFrame format
        indicator_df = pd.DataFrame(data)
        if not indicator_df.empty:
            # Extract relevant columns
            indicator_df = indicator_df[['country', 'date', 'value']]
            indicator_df['indicator'] = indicator_name
            all_data.append(indicator_df)
        
        # Be nice to the API with rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"Error fetching {indicator_name}: {e}")

# Combine all the data
if all_data:
    data = pd.concat(all_data, ignore_index=True)
    
    # Save raw data
    data.to_csv('data/raw/wdi_raw_data.csv', index=False)
    print(f"Raw data saved with {len(data)} records")
    
    # 5. Reshape dataframe to wide format for analysis
    try:
        # Convert date to datetime
        data['date'] = pd.to_datetime(data['date'])
        # Get just the year
        data['year'] = data['date'].dt.year
        
        # Drop the original date column and pivot
        data_clean = data.drop('date', axis=1).pivot_table(
            index=['country', 'year'], 
            columns='indicator', 
            values='value'
        ).reset_index()
        
        # Calculate additional metrics
        if 'education_exp' in data_clean.columns and 'govt_expenditure' in data_clean.columns:
            data_clean['education_share'] = data_clean['education_exp'] / data_clean['govt_expenditure']
        
        if 'health_exp' in data_clean.columns and 'govt_expenditure' in data_clean.columns:
            data_clean['health_share'] = data_clean['health_exp'] / data_clean['govt_expenditure']
        
        # Save processed data
        data_clean.to_csv('data/processed/middle_income_policy_data.csv', index=False)
        
        print(f"Dataset contains {data_clean['country'].nunique()} countries, from {data_clean['year'].min()} to {data_clean['year'].max()}")
        print(f"Processed data saved to data/processed/middle_income_policy_data.csv")
        
        # Generate a quick summary of data completeness
        completeness = data_clean.count() / len(data_clean) * 100
        completeness = completeness.sort_values(ascending=False)
        
        with open('data/processed/data_completeness_summary.txt', 'w') as f:
            f.write("Data Completeness Summary (% of non-missing values)\n")
            f.write("="*50 + "\n")
            for col, pct in completeness.items():
                f.write(f"{col}: {pct:.1f}%\n")
        
        print("Data collection complete!")
        
    except Exception as e:
        print(f"Error processing data: {e}")
else:
    print("No data collected. Please check for errors above.")

print("\nNext steps:")
print("1. Review data_completeness_summary.txt to understand data availability")
print("2. Proceed with exploratory data analysis")
print("3. Run varying coefficient model estimations")
