import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.title("Weather Prediction App")

st.set_page_config(page_title="Weather Prediction", page_icon="🌤️", layout="centered")

st.caption("This app predicts the Weather Forecasting")

st.divider()

model = joblib.load('weather_model.pkl')

col1, col2 = st.columns(2)

with col1:
    humidity3pm = st.number_input(
        "Humidity 3 PM (%)",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )

    Sunshine = st.number_input(
        "Sunshine (hrs)",
        min_value=0.0,
        max_value=24.0,
        value=6.0,
        step=0.5
    )

    pressure3pm = st.number_input(
        "Pressure 3 PM",
        min_value=900.0,
        max_value=1100.0,
        value=1013.0,
        step=0.5
    )

    cloud9am = st.number_input(
        "Cloud 9 AM",
        min_value=0.0,
        max_value=8.0,
        value=4.0,
        step=0.5
    )

    humidity9am = st.number_input(
        "Humidity 9 AM",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.5
    )

with col2:
    Rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=0.0,
        step=0.5
    )

    Cloud3pm = st.number_input(
        "Cloud 3 PM",
        min_value=0.0,
        max_value=8.0,
        value=4.0,
        step=0.5
    )

    windgustspeed = st.number_input(
        "Wind Gust Speed",
        min_value=0.0,
        max_value=150.0,
        value=10.0,
        step=0.5
    )

    pressure9am = st.number_input(
        "Pressure 9 AM",
        min_value=900.0,
        max_value=1100.0,
        value=1013.0,
        step=0.5
    )

    raintoday = st.selectbox(
        "Rain Today",
        ["No", "Yes"]
    )

if st.button("Predict"):
    input_data = pd.DataFrame({
        'humidity3pm': [humidity3pm],
        'Rainfall': [Rainfall],
        'Sunshine': [Sunshine],
        'Cloud3pm': [Cloud3pm],
        'pressure3pm': [pressure3pm],
        'windgustspeed': [windgustspeed],
        'cloud9am': [cloud9am],
        'pressure9am': [pressure9am],
        'humidity9am': [humidity9am],
        'raintoday_Yes': [1 if raintoday == "Yes" else 0]
    })

    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.success("It will Rain Tomorrow 🌧️")
    else:
        st.success("No Rain Tomorrow ☀️")

    st.subheader("Prediction Probability")
    st.write(f"Probability of Rain: {prediction_proba[0][1]:.2f}")
    st.write(f"Probability of No Rain: {prediction_proba[0][0]:.2f}")