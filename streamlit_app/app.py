import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the data

data = pd.read_csv("diabetes.csv")
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train the model
model = DecisionTreeClassifier()
model.fit(x, y)


# Prediction function
def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    features = np.asarray([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    features = features.reshape(1, -1)
    prediction = model.predict(features)
    return "Having diabetes" if prediction == 1 else "Not Having diabetes"

# Streamlit UI
st.title('DIABETES PREDICTION')
Pregnancies = st.number_input('Pregnancies')
Glucose = st.number_input('Glucose')
BloodPressure = st.number_input('BloodPressure')
SkinThickness = st.number_input('SkinThickness')
Insulin = st.number_input('Insulin')
BMI = st.number_input('BMI')
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
Age = st.number_input('Age')

if st.button('Predict'):
    prediction = predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    st.write(f"PREDICTION: {prediction}")
