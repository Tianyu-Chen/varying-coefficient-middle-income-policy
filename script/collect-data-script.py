"""
Data Collection Script for Middle-Income Countries Policy Analysis

This script collects World Bank Development Indicators data for middle-income
countries, focusing on economic policies and growth indicators from 2000-2020.
"""
from pandas_datareader import wb
# Economic indicators
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
}

data = wb.download(indicator=indicators, country=['DZA', 'AGO', 'BGD', 'BLZ', 'BEN', 'BTN', 'BOL', 'KHM', 'CMR', 'CPV', 
             'COM', 'COG', 'CIV', 'DJI', 'EGY', 'SLV', 'SWZ', 'GHA', 'HND', 'IND', 
             'IDN', 'IRN', 'KEN', 'KIR', 'KGZ', 'LAO', 'LSO', 'MRT', 'FSM', 'MNG', 
             'MAR', 'MMR', 'NIC', 'NGA', 'PAK', 'PNG', 'PHL', 'WSM', 'STP', 'SEN', 
             'SLB', 'LKA', 'TZA', 'TLS', 'TUN', 'UKR', 'UZB', 'VUT', 'VNM', 'PSE', 
             'ZMB', 'ZWE', 'ALB', 'ARG', 'ARM', 'AZE', 'BLR', 'BIH', 'BWA', 'BRA', 
             'BGR', 'CHN', 'COL', 'CRI', 'CUB', 'DMA', 'DOM', 'ECU', 'GNQ', 'FJI', 
             'GAB', 'GEO', 'GRD', 'GTM', 'GUY', 'IRQ', 'JAM', 'JOR', 'KAZ', 'XKX', 
             'LBN', 'LBY', 'MYS', 'MDV', 'MHL', 'MUS', 'MEX', 'MDA', 'MNE', 'NAM', 
             'MKD', 'PRY', 'PER', 'ROU', 'RUS', 'SRB', 'ZAF', 'LCA', 'VCT', 'SUR', 
             'THA', 'TON', 'TUR', 'TKM', 'TUV'] , 
                   start=2000, end=2020)
data.to_csv('world_bank_data.csv')