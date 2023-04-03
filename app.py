import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model_churn.pkl')

# Create a Streamlit app
def app():
    st.title('Telecom Company Churn Prediction')
    st.write('Enter the following customer details to predict churn')

    # Get user input
    gender = st.selectbox('Gender', ['Male', 'Female'])
    seniorcitizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
    partner = st.selectbox('Partner', ['Yes', 'No'])
    dependents = st.selectbox('Dependents', ['Yes', 'No'])
    tenure = st.slider('Tenure (months)', 0, 72, 12)
    monthlycharges = st.slider('Monthly Charges', 0, 200, 50)
    totalcharges = st.slider('Total Charges', 0, 8000, 2000)
    contract = st.selectbox('Contract', ['Month-to-Month', 'One Year', 'Two Year'])
    paymentmethod = st.selectbox('Payment Method', ['Electronic Check', 'Mailed Check', 'Bank Transfer (Auto)', 'Credit Card (Auto)'])

    # Preprocess user input
    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    if seniorcitizen == 'Yes':
        seniorcitizen = 1
    else:
        seniorcitizen = 0

    if partner == 'Yes':
        partner = 1
    else:
        partner = 0

    if dependents == 'Yes':
        dependents = 1
    else:
        dependents = 0

    if contract == 'Month-to-Month':
        contract_monthly = 1
        contract_one_year = 0
        contract_two_year = 0
    elif contract == 'One Year':
        contract_monthly = 0
        contract_one_year = 1
        contract_two_year = 0
    else:
        contract_monthly = 0
        contract_one_year = 0
        contract_two_year = 1

    if paymentmethod == 'Electronic Check':
        paymentmethod_electronic_check = 1
        paymentmethod_mailed_check = 0
        paymentmethod_bank_transfer_auto = 0
        paymentmethod_credit_card_auto = 0
    elif paymentmethod == 'Mailed Check':
            paymentmethod_electronic_check = 0
    paymentmethod_mailed_check = 1
    paymentmethod_bank_transfer_auto = 0
    paymentmethod_credit_card_auto = 0
elif paymentmethod == 'Bank Transfer (Auto)':
paymentmethod_electronic_check = 0
paymentmethod_mailed_check = 0
paymentmethod_bank_transfer_auto = 1
paymentmethod_credit_card_auto = 0
else:
paymentmethod_electronic_check = 0
paymentmethod_mailed_check = 0
paymentmethod_bank_transfer_auto = 0
paymentmethod_credit_card_auto = 1

# Make prediction using the model
prediction = model.predict([[gender, seniorcitizen, partner, dependents, tenure, monthlycharges, totalcharges, contract_monthly, contract_one_year, contract_two_year, paymentmethod_electronic_check, paymentmethod_mailed_check, paymentmethod_bank_transfer_auto, paymentmethod_credit_card_auto]])

# Display the prediction
if prediction == 1:
    st.write('This customer is likely to churn')
else:
    st.write('This customer is not likely to churn')


if name == 'main':
app()






____________________________________________---------------------------------------------___________________________________


