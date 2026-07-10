# 🌦 Australian Weather Prediction

A machine learning web application that predicts whether it will rain tomorrow using historical Australian weather data.

The model is deployed using Streamlit.


## 🚀 Live Demo

Streamlit App:

https://appweatherprediction-stydz8sdfhdth5dcknirnm.streamlit.app/
---

## 📌 Problem Statement

Weather prediction is a classification problem where the goal is to predict whether rainfall will occur the next day based on current weather conditions.

Target variable:

RainTomorrow

Values:
- Yes → Rain expected
- No → No rain expected


## 📊 Dataset

Dataset:
Australian Weather Dataset

Source:
Kaggle

Dataset contains weather observations from different locations in Australia.

Features include:

- Humidity
- Rainfall
- Sunshine
- Cloud coverage
- Pressure
- Wind speed
- Temperature etc,


## 🛠️ Technologies Used

Programming Language:
- Python

Libraries:
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit



## ⚙️ Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Missing Value Handling
5. Feature Encoding
6. Model Training
7. Model Evaluation
8. Model Deployment



## 🤖 Model Used

Algorithm:

Random Forest Classifier 
ExtraTree Classifier


Reason for choosing Random Forest:

- Handles nonlinear relationships
- Handles multicollinarity 
- Works well with mixed features
- Reduces overfitting compared to single decision trees




## 📈 Model Performance

Metrics: 1.Accuracy  2.Classification report

Accuracy: 84.2%

Precision: 76%

Recall: 47%

F1 Score: 58%


## 📂 Project Structure

- .venv
- .gitignore
- app.py
- Notebook.ipynb
- requirements.txt
- runtime.txt
- weather_model.pkl
- README.md