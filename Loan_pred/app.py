# app.py
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🏦 Loan Approval Prediction App")
st.write("Enter the applicant details below to predict loan approval.")

# Input fields
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode inputs manually (same as training)
def encode_inputs():
    data = {
        'Gender': 1 if Gender == "Male" else 0,
        'Married': 1 if Married == "Yes" else 0,
        'Dependents': 3 if Dependents == "3+" else int(Dependents),
        'Education': 0 if Education == "Graduate" else 1,
        'Self_Employed': 1 if Self_Employed == "Yes" else 0,
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Property_Area': 2 if Property_Area == "Urban" else (1 if Property_Area == "Semiurban" else 0)
    }
    return pd.DataFrame([data])

# Prediction
if st.button("Predict Loan Status"):
    input_data = encode_inputs()

    # Standardize numeric columns
    num_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan will be Approved!")
    else:
        st.error("❌ Loan will be Rejected.")
