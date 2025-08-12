# COVID-19 Community Data Analysis for Alberta Cities

A comprehensive dataset and analysis toolkit for COVID-19 impact on Calgary and Edmonton communities, combining demographic profiles with pandemic metrics.

## 📋 Overview

This repository provides cleaned and processed COVID-19 data for Alberta's major cities (Calgary and Edmonton), integrated with community demographic profiles. The data supports research into the relationship between community characteristics and pandemic outcomes.

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Jupyter Notebook
- Required packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `requests`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/r-hedayati/PublicData.git
   cd PublicData
   ```

2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn requests
   ```

3. Run the data scraper (optional - data files are already included):

   ```bash
   python codes/public_data_scrapper.py
   ```

### Usage

1. **Data Preprocessing**: Open `codes/PublicData_Preprocessing.ipynb` to see how raw data is cleaned and combined
2. **Time Series Analysis**: Use `codes/PublicData_TimeAnalysis.ipynb` for temporal analysis of COVID-19 trends

## 📊 Dataset Description

Each CSV file contains integrated data across four main categories:

### 1. **Community Profile Features**

- **Demographics**: Population, age groups (0-14, 15-64, 65-84, 85+), gender distribution
- **Household**: Average household size, family composition
- **Immigration**: Non-immigrants, immigrants, recent immigrants, non-permanent residents, aboriginal population
- **Education**: Educational attainment levels (no certificate, high school, post-secondary)
- **Employment**: Labour participation rate, employment rate
- **Transportation**: Transportation modes (driver+passenger, public transit, walking+biking)
- **Economic**: Low income indicators

### 2. **COVID-19 Cases**

- Active cases
- Recovered cases  
- Total cumulative cases
- Deaths

### 3. **COVID-19 Vaccines**

- First dose administered
- Second dose administered
- Total doses administered

### 4. **COVID-19 Outbreaks**

- Total outbreaks (schools + other facilities)

## 📁 Data Files

| File | Description | Geographic Unit |
|------|-------------|-----------------|
| `calgary_data.csv` | Calgary communities data with proportionally assigned COVID-19 metrics | Community |
| `edmonton_data.csv` | Edmonton communities data with proportionally assigned COVID-19 metrics | Community |
| `calgary_data_LHA.csv` | Calgary data aggregated by Alberta Health Services Local Health Areas | LHA |
| `edmonton_data_LHA.csv` | Edmonton data aggregated by Alberta Health Services Local Health Areas | LHA |
| `All_data_LHA.csv` | Combined Calgary and Edmonton data by Local Health Areas | LHA |
| `All_data.csv` | Combined Calgary and Edmonton community-level data | Community |

## 🔧 Code Structure

```text
codes/
├── public_data_scrapper.py          # Data collection from public APIs
├── PublicData_Preprocessing.ipynb   # Data cleaning and integration
└── PublicData_TimeAnalysis.ipynb    # Temporal analysis and visualization

input/
├── CommunityProfileData.xlsx        # Raw community demographic data
├── calgary_covid.csv               # Calgary COVID-19 raw data
├── edmonton_covid.csv              # Edmonton COVID-19 raw data
├── outbreakPlaces.csv              # Outbreak location data
└── schoolsOutbreak.csv             # School outbreak data
```

## 📈 Data Sources

- **COVID-19 Data**: [COVID-19 Canada Open Data Working Group](https://github.com/ccodwg/Covid19Canada)
- **Alberta Health Data**: Alberta Government Open Data Portal
- **Community Profiles**: Statistics Canada Census Data
- **Vaccination Data**: Alberta Health Services

## 🔬 Research Applications

This dataset is suitable for:

- **Epidemiological Analysis**: Understanding COVID-19 spread patterns
- **Social Determinants Research**: Examining how community characteristics influence health outcomes
- **Public Health Policy**: Evidence-based decision making for targeted interventions
- **Geospatial Analysis**: Mapping disease patterns and community vulnerabilities

## 📝 Citation

If you use this dataset in your research, please cite:

```bibtex
[Your Name]. (2025). COVID-19 Community Data Analysis for Alberta Cities. 
GitHub repository: https://github.com/r-hedayati/PublicData
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: COVID-19 data is proportionally assigned to communities based on population distribution where direct community-level data is not available.
**Disclaimer**: The data provided is for research purposes only and should not be used for clinical decision-making. Always refer to official health sources for the most current information.