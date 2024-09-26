import streamlit as st
import pandas as pd
import pickle

# Load the trained Lasso model
filename = 'quiz.py'
loaded_model = pickle.load(open(filename, 'rb'))

# Create the Streamlit app
st.title("Monthly Revenue Prediction")

# Input features
st.header("Enter Store Features")

# Get user input for features
total_orders = st.number_input("Total Orders", min_value=0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", min_value=0.0)
customer_lifetime_value = st.number_input("Customer Lifetime Value", min_value=0.0)
average_order_frequency = st.number_input("Average Order Frequency", min_value=0.0)
marketing_spend = st.number_input("Marketing Spend", min_value=0.0)
total_customers = st.number_input("Total Customers", min_value=0)


# Create a button to predict revenue
if st.button("Predict Monthly Revenue"):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        "total_orders": [total_orders],
        "avg_order_value": [avg_order_value],
        "customer_acquisition_cost": [customer_acquisition_cost],
        "customer_lifetime_value": [customer_lifetime_value],
        "average_order_frequency": [average_order_frequency],
        "marketing_spend": [marketing_spend],
        "total_customers": [total_customers],
    })

    # Make a prediction using the loaded model
    predicted_revenue = loaded_model.predict(input_data)[0]

    # Display the predicted revenue
    st.subheader(f"Predicted Monthly Revenue: ${predicted_revenue:.2f}")

