# 🌤️ Weather Data Analysis Project

> **A comprehensive Flask web application for analyzing weather data with interactive visualizations and statistical insights**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents
- [Overview](#overview)
- [Project Aim](#project-aim)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Format](#data-format)
- [Statistical Analysis](#statistical-analysis)
- [Visualizations](#visualizations)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The Weather Data Analysis Project is a modern web application designed to help users analyze weather patterns through an intuitive interface. Upload your weather data via CSV file or paste it directly, and instantly receive comprehensive statistical analysis with beautiful, interactive visualizations.

This application processes **daily temperature and rainfall data** to compute central tendency measures, standard deviation, visualize trends, and statistically test whether average temperatures differ significantly across months using ANOVA.

### Why This Project?

- 📊 **Educational**: Perfect for students learning data analysis and statistics
- 🔬 **Research**: Useful for climate research and weather pattern studies
- 💼 **Professional**: Can be extended for business weather analytics
- 🚀 **Modern**: Built with latest web technologies and best practices

## 🎓 Project Aim

This project fulfills the following statistical analysis objectives:

1. ✅ **Use daily temperature/rainfall data** - Process time-series weather data
2. ✅ **Compute central tendency** - Calculate mean, median, and mode
3. ✅ **Compute standard deviation (SD)** - Measure data dispersion
4. ✅ **Visualize trends** - Create interactive charts for pattern analysis
5. ✅ **Statistical testing** - ANOVA test to determine if average temperature differs significantly across months

## ✨ Features

### 📤 Flexible Data Input
- **File Upload**: Drag & drop or browse to upload CSV files
- **Manual Input**: Paste CSV data directly into a text area
- **Format Validation**: Automatic validation with helpful error messages
- **Sample Format**: Visual guide showing the expected CSV structure

### 🧮 Statistical Analysis
- **Descriptive Statistics**:
  - Mean (average) temperature
  - Median temperature
  - Mode (most frequent temperature)
  - Standard deviation
- **Monthly Analysis**:
  - Mean, standard deviation, min, and max per month
  - Interactive monthly comparison
- **Hypothesis Testing**:
  - ANOVA (Analysis of Variance) test
  - F-statistic and p-value calculation
  - Automatic interpretation at α = 0.05 significance level

### 📊 Interactive Visualizations
- **Daily Temperature Trend**: Line chart showing temperature over time
- **Monthly Temperature Bar Chart**: Compare average temperatures across months
- **Daily Rainfall Trend**: Area chart visualizing precipitation patterns
- **All charts support**: Zoom, pan, hover for details, download as PNG

### 🔒 Privacy & Performance
- **In-Memory Processing**: No files saved to disk
- **Session-Based**: Each user's data is isolated
- **Auto-Cleanup**: Data cleared when session ends
- **Fast Processing**: Instant analysis and visualization

### 🎨 User Experience
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Beautiful UI**: Modern gradient design with Bootstrap 5
- **Intuitive Navigation**: Clear workflow from upload to results
- **Error Handling**: Friendly error messages guide users

## 🛠️ Tech Stack

### Backend
- **Flask 3.0+** - Python web framework
- **pandas 2.1+** - Data manipulation and analysis
- **scipy 1.11+** - Statistical computations (ANOVA)
- **Plotly 5.18+** - Interactive visualizations

### Frontend
- **Bootstrap 5** - Responsive UI framework
- **Plotly.js** - Interactive chart rendering
- **HTML5/CSS3** - Modern web standards

### Architecture
- **Session-based storage** - Flask sessions for temporary data
- **In-memory processing** - No file system dependencies
- **RESTful design** - Clean API endpoints

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pas-weather-project.git
   cd pas-weather-project
   ```

2. **Create a virtual environment**
   ```bash
   # On Linux/Mac
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import flask, pandas, plotly, scipy; print('All dependencies installed!')"
   ```

## 🚀 Usage

### Starting the Application

1. **Activate virtual environment** (if not already activated)
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Run the Flask application**
   ```bash
   python app.py
   ```

3. **Open your browser**
   Navigate to: `http://localhost:5000`

### Using the Application

#### Option 1: Upload CSV File
1. Click on the **"📁 Upload File"** tab
2. Drag and drop your CSV file, or click **"Browse Files"**
3. Wait for validation (instant feedback)
4. Click **"Analyze Data"** button
5. View your interactive dashboard

#### Option 2: Paste CSV Data
1. Click on the **"✏️ Paste CSV"** tab
2. Paste your CSV data (including headers)
3. Click **"Analyze Data"** button
4. View your interactive dashboard

### Example CSV Data

Here's a sample to get you started:

```csv
Date,Temperature,Rainfall
2024-01-01,25.5,0.0
2024-01-02,26.3,2.5
2024-01-03,24.8,5.2
2024-01-04,27.1,0.0
2024-01-05,26.9,1.3
```

## 📁 Project Structure

```
pas-weather-project/
│
├── app.py                      # Main Flask application
├── weather_analysis.py         # Analysis logic and chart generation
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this file)
├── .gitignore                 # Git ignore rules
│
├── templates/                 # HTML templates
│   ├── upload.html           # Upload/input page
│   └── results.html          # Results dashboard
│
└── venv/                      # Virtual environment (not in git)
```

### Key Files Explained

- **`app.py`**: Flask routes, file/text handling, validation, session management
- **`weather_analysis.py`**: Data processing, statistical calculations, Plotly chart generation
- **`templates/upload.html`**: Landing page with file upload and manual input tabs
- **`templates/results.html`**: Dashboard displaying statistics and charts

## 📊 Data Format

### Required Columns

Your CSV file **must** contain these three columns:

| Column Name | Data Type | Description | Example |
|-------------|-----------|-------------|----------|
| `Date` | Date/String | Date of observation | 2024-01-01 |
| `Temperature` | Numeric | Temperature in °C | 25.5 |
| `Rainfall` | Numeric | Rainfall in mm | 2.5 |

### Format Requirements

- **Headers**: First row must contain column names exactly as shown
- **Date Format**: Any parseable format (YYYY-MM-DD recommended)
- **Numeric Values**: Use decimal points (not commas)
- **File Size**: Maximum 16 MB
- **Encoding**: UTF-8 (standard)

### Valid Example

```csv
Date,Temperature,Rainfall
2024-01-01,25.5,0.0
2024-01-02,26.3,2.5
2024-01-03,24.8,5.2
```

### Invalid Examples

❌ Missing required column:
```csv
Date,Temperature
2024-01-01,25.5
```

❌ Wrong column names:
```csv
date,temp,rain
2024-01-01,25.5,0.0
```

❌ Non-numeric values:
```csv
Date,Temperature,Rainfall
2024-01-01,hot,none
```

## 🔬 Statistical Analysis

### Descriptive Statistics

The application calculates:

1. **Mean (μ)**: Average temperature across all days
   ```
   μ = Σx / n
   ```

2. **Median**: Middle value when data is sorted

3. **Mode**: Most frequently occurring temperature

4. **Standard Deviation (σ)**: Measure of temperature variability
   ```
   σ = √[Σ(x - μ)² / n]
   ```

### Monthly Analysis

Data is grouped by month to compute:
- Monthly mean temperature
- Monthly standard deviation
- Monthly minimum and maximum

### Hypothesis Testing (ANOVA)

**Research Question**: Does average temperature differ significantly across months?

- **Null Hypothesis (H₀)**: All monthly means are equal
- **Alternative Hypothesis (H₁)**: At least one monthly mean differs
- **Test**: One-way ANOVA (Analysis of Variance)
- **Significance Level**: α = 0.05

**Interpretation**:
- If **p-value < 0.05**: Reject H₀ (significant difference exists)
- If **p-value ≥ 0.05**: Fail to reject H₀ (no significant difference)

## 📈 Visualizations

### 1. Daily Temperature Trend
- **Type**: Line chart
- **X-axis**: Date
- **Y-axis**: Temperature (°C)
- **Purpose**: Identify temperature patterns over time
- **Features**: Hover for exact values, zoom, pan

### 2. Monthly Average Temperature
- **Type**: Bar chart
- **X-axis**: Month (1-12)
- **Y-axis**: Average Temperature (°C)
- **Purpose**: Compare temperature across months
- **Features**: Interactive bars with tooltips

### 3. Daily Rainfall Trend
- **Type**: Area chart
- **X-axis**: Date
- **Y-axis**: Rainfall (mm)
- **Purpose**: Visualize precipitation patterns
- **Features**: Filled area for better visibility

### Chart Interactions

All charts support:
- 🔍 **Zoom**: Click and drag to zoom into specific areas
- 🖱️ **Pan**: Shift + drag to pan across data
- 📌 **Hover**: See exact values on hover
- 💾 **Download**: Save charts as PNG images
- 🔄 **Reset**: Double-click to reset view

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run in debug mode
export FLASK_ENV=development
python app.py
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Developed with ❤️ for weather data analysis

## 🙏 Acknowledgments

- **Flask** - Lightweight and powerful web framework
- **Plotly** - Beautiful interactive visualizations
- **pandas** - Robust data manipulation
- **scipy** - Scientific computing tools
- **Bootstrap** - Responsive UI components

## 📞 Support

If you encounter any issues or have questions:
1. Check existing [Issues](https://github.com/yourusername/pas-weather-project/issues)
2. Open a new issue with detailed description
3. Include error messages and steps to reproduce

---

**Happy Analyzing! 🌤️📊**
