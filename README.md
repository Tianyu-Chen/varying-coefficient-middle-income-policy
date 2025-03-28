# Varying Coefficient Models for Economic Development

## Project Overview

This project investigates how the effectiveness of different economic policies (investment, education spending, etc.) varies across development stages in middle-income countries. Many developing nations experience a "middle-income trap" where strategies that worked well for reaching middle-income status fail to propel them to high-income status.

We apply varying coefficient models to World Bank Development Indicators to analyze how policy effects change with development level, potentially providing insights into optimizing policy portfolios at different development stages.

## Research Questions

1. How does the impact of different economic policies (education, healthcare, infrastructure investment, etc.) vary with a country's development level?
2. Which policies are most effective for middle-income countries at different stages of development?
3. Is there evidence for changing policy priorities as countries progress through the middle-income range?

## Methodology

We employ varying coefficient models of the form:

```
Y_{it} = β₀(U_{it}) + Σ βⱼ(U_{it})X_{j,it} + ε_{it}
```

where:
- Y_{it} is GDP growth rate for country i in year t
- X_{j,it} represents policy variables (education spending, etc.)
- U_{it} is development level (GDP per capita)
- β_j(U_{it}) are coefficient functions that vary with development level
- ε_{it} is a random error term

The model is estimated using kernel-local polynomial smoothing methods.

## Data Sources

- **World Bank Development Indicators**: Economic metrics, policy variables, and development indicators
- **Human Development Index (HDI)**: Alternative development measure incorporating education and health
- **World Governance Indicators**: Institutional quality metrics

## Repository Structure

```
vc-economic-development/
├── README.md                  # Project overview and documentation
├── LICENSE                    # MIT License
├── .gitignore                 # Specifies intentionally untracked files
├── requirements.txt           # Python dependencies
├── scripts/                   # Python scripts
│   ├── collect_wdi_data.py    # Data collection from World Bank API
│   ├── exploratory_analysis.py # Initial data exploration
│   └── vc_estimation.py       # Varying coefficient model implementation
├── data/                      # Data directory
│   ├── raw/                   # Raw data files
│   │   └── middle_income_countries.csv  # List of countries with classifications
│   └── processed/             # Processed datasets
│       └── middle_income_policy_data.csv # Clean, analysis-ready data
└── results/                   # Results and outputs
    ├── figures/               # Generated visualizations
    │   ├── gdp_per_capita_distribution.png # Income distribution
    │   └── growth_by_income_level.png     # Growth rate comparisons
    └── tables/                # Output tables and statistics
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.gatech.edu/tchen474/vc-economic-development.git
cd vc-economic-development
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

### Data Collection

Run the data collection script to fetch World Bank Development Indicators:
```bash
python scripts/collect_wdi_data.py
```
This script will:
- Identify middle-income countries
- Collect economic and policy indicators from 2000-2020
- Process and save the data for analysis

### Analysis

Perform exploratory data analysis:
```bash
python scripts/exploratory_analysis.py
```

Run the varying coefficient model estimation:
```bash
python scripts/vc_estimation.py
```

## Model Features

The varying coefficient model implementation includes:
- Multiple kernel options (Gaussian, Epanechnikov)
- Bandwidth selection procedures
- Visualization of coefficient functions
- Analysis of policy effectiveness at different development levels

## Team Members

- Tianyu Chen
- Xinjie Zhu
- Jingyun Sun
- Xiangchi Ye

## Citation

If you use this project in your research, please cite:
```
Chen, T., Zhu, X., Sun, J., & Ye, X. (2025). Varying Coefficient Models for Economic Development.
GitHub repository, https://github.gatech.edu/tchen665/vc-economic-development
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
