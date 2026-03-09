import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the AI Model
model = joblib.load('kerala_pm25_model.pkl')

# 2. Design the Web Page
st.set_page_config(page_title="Kerala Air Quality AI", page_icon="🍃")
st.title("🍃 Northern Kerala PM2.5 Predictor")
st.write("Enter the hyper-local weather conditions below to predict particulate matter levels.")

# 3. Create Input Sliders & Dropdowns for the User
st.sidebar.header("Input Parameters")

location = st.sidebar.selectbox("Select Town", ["Keezhur", "Therthally", "Other"])
temp = st.sidebar.slider("Temperature (°C)", 20.0, 45.0, 30.0)
humidity = st.sidebar.slider("Humidity (%)", 30.0, 100.0, 75.0)
rain = st.sidebar.slider("Rainfall (mm)", 0.0, 150.0, 10.0)
wind = st.sidebar.slider("Wind Speed (m/s)", 0.0, 20.0, 5.0)

# 4. Format the Data for the AI
# The AI needs the exact same columns it was trained on!
is_keezhur = 1 if location == "Keezhur" else 0
is_therthally = 1 if location == "Therthally" else 0

input_data = pd.DataFrame({
    'Temp_C': [temp],
    'Humidity_pct': [humidity],
    'Rainfall_mm': [rain],
    'WindSpeed_ms': [wind],
    'Location_Keezhur': [is_keezhur],
    'Location_Therthally': [is_therthally]
})

# 5. Make the Prediction
if st.button("Predict PM2.5 Level"):
    with st.spinner("Analyzing atmospheric data..."):
        prediction = model.predict(input_data)[0]
        
        st.subheader("Predicted PM2.5 Concentration:")
        
        # Color code the result based on safety!
        if prediction < 30:
            st.success(f"🟢 {prediction:.2f} µg/m³ (Good)")
        elif prediction < 60:
            st.warning(f"🟡 {prediction:.2f} µg/m³ (Moderate)")
        else:
            st.error(f"🔴 {prediction:.2f} µg/m³ (Unhealthy)")
            
        st.write("---")
        st.caption("Powered by XGBoost Machine Learning")