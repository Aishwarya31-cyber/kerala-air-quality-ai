# 🍃 Air Quality (PM2.5) Predictor: Northern Kerala

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kerala-air-quality-ai.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![XGBoost](https://img.shields.io/badge/Machine%20Learning-XGBoost-orange)](https://xgboost.readthedocs.io/)

A full-stack Machine Learning web application that predicts hyper-local Particulate Matter (PM2.5) concentrations in Northern Kerala based on meteorological parameters and spatial data.

**👉 [Try the Live Web App Here!](https://kerala-air-quality-ai.streamlit.app/)**

---

## 🎯 Project Overview
Air pollution modeling often relies on heavy, expensive hardware. This Proof-of-Concept (PoC) project demonstrates how computationally lightweight, tree-based machine learning algorithms can accurately predict baseline air quality strictly using weather data (meteorology) and spatial tagging.

This project was built using real-world sensor data from the towns of **Keezhur** and **Therthally** in Kerala, India.

## 🔬 The Data Engineering Pipeline
Real-world Excel (`.xlsx`) sensor logs were processed through a custom Python pipeline:
1. **Automated Extraction:** Aggregated multiple monthly datasets into a single Pandas DataFrame.
2. **Regex Cleaning:** Stripped hidden text, symbols, and averaged high/low metrics into pure float values.
3. **Spatial Tagging (One-Hot Encoding):** Dynamically extracted location data from file names to give the AI spatial awareness of distinct micro-climates.
4. **Imputation:** Handled missing rainfall parameters with domain-specific default logic.

## 🧠 Machine Learning Model
The core predictive engine is an **XGBoost Regressor**, chosen for its high performance on tabular data and its intrinsic resistance to out-of-bounds extrapolation. 

### Model Performance (Real Sensor Data)
* **$R^2$ Score:** `~ 0.45` 
* **RMSE:** `~ 10.31 µg/m³`

*Note on Accuracy:* The $R^2$ of 0.45 proves that **45% of air pollution variance is driven purely by the weather**. The remaining variance represents human activity (traffic, industry), making this a highly realistic meteorological baseline model.

## 📊 Explainable AI (SHAP Insights)
To break the "black box" of the AI, we used **SHAP (SHapley Additive exPlanations)** to extract the underlying atmospheric physics learned by the model:

1. **Humidity is the #1 Driver:** The model correctly learned that high humidity swells microscopic aerosols, trapping PM2.5 closer to the ground.
2. **Temperature as a Disperser:** Thermal convection was validated—higher temperatures correlate with lower local PM2.5 as hot air rises and disperses particulates.
3. **The Wash-Out Effect:** Rainfall negatively impacts PM2.5 by physically scrubbing the air clean.
4. **Spatial Baselines:** The AI successfully differentiated the intrinsic geographical pollution baselines between Keezhur and Therthally.

## 💻 Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy, Regex
* **Machine Learning:** XGBoost, Scikit-Learn
* **Explainable AI:** SHAP, Matplotlib
* **Web Deployment:** Streamlit Community Cloud

---

## 🚀 How to Run Locally

If you want to run this AI on your own machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/kerala-air-quality-ai.git](https://github.com/YOUR_GITHUB_USERNAME/kerala-air-quality-ai.git)
