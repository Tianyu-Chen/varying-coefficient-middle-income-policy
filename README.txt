# Policy Effectiveness Across Development Stages in Middle-Income Countries

This project investigates how the effects of different economic policies (investment, education spending, etc.) vary across development stages, with a specific focus on middle-income countries. We use the World Bank Development Indicators as our primary dataset and apply varying coefficient models to analyze policy effectiveness.

## Project Overview

The "middle-income trap" suggests that strategies that work well for countries to reach middle-income status may not be sufficient to propel them to high-income status. This project applies varying coefficient models to systematically analyze how the effectiveness of different economic policies varies with development stages in middle-income countries.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/vc-economic-development.git
cd vc-economic-development

# Install dependencies
pip install -r requirements.txt

# Run data collection script
python scripts/collect_wdi_data.py

# Run exploratory data analysis
python scripts/exploratory_analysis.py

# Run model estimation
python scripts/vc_estimation.py
```

## Data

This project uses data from:

- **World Bank Development Indicators**: Economic, policy, and development metrics
- **Human Development Index**: For a broader measure of development
- **World Governance Indicators**: Institutional quality measures

The main variables include:
- **Dependent Variable**: Annual GDP growth rate
- **Policy Variables**: Education spending, health expenditure, R&D investment, etc.
- **Moderating Variable**: GDP per capita or Human Development Index

## Data Collection

The `scripts/collect_wdi_data.py` script automatically fetches all necessary data from the World Bank API. It:

1. Identifies middle-income countries (both lower-middle and upper-middle)
2. Collects economic indicators, policy variables, and governance metrics from 2000-2020
3. Processes and saves both raw and clean versions of the data
4. Generates a summary of data completeness

## Methodology

We employ varying coefficient models of the form:

$$Y = X^T a(U) + \epsilon$$

where:
- $Y$ is a country's annual growth rate
- $X$ is a vector of policy variables
- $a(U)$ are functional coefficients that vary with development level $U$
- $\epsilon$ is a random error term

The kernel-local polynomial smoothing method is used for estimation, allowing us to visualize how policy effects change with development level.

## Project Structure

```
vc-economic-development/
├── scripts/                 # Data collection and analysis scripts
├── data/                    # Data storage
│   ├── raw/                 # Raw data files
│   └── processed/           # Processed datasets
├── models/                  # Model implementation code
├── results/                 # Results and visualizations
│   ├── figures/             # Generated figures
│   └── tables/              # Generated tables
└── docs/                    # Documentation
```

## Team Members

- Tianyu Chen
- Xinjie Zhu
- Jingyun Sun
- Xiangchi Ye

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
