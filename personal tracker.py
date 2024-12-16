import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.title("Personal Expense Tracker")
st.markdown("Track your income and expenses easily!")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Type", "Category", "Amount", "Date"])

# Expense categories
categories = ["Food", "Rent", "Utilities", "Transport", "Entertainment", "Other"]

# Add new transaction
st.header("Add New Transaction")
transaction_type = st.radio("Type", ["Income", "Expense"])
category = st.selectbox("Category", categories if transaction_type == "Expense" else ["Salary", "Business", "Other"])
amount = st.number_input("Amount", min_value=0.0, step=0.01)
date = st.date_input("Date")
add_transaction = st.button("Add Transaction")

if add_transaction:
    if amount > 0:
        # Append transaction to the session state
        new_data = {"Type": transaction_type, "Category": category, "Amount": amount, "Date": str(date)}
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_data])], ignore_index=True)
        st.success("Transaction added successfully!")
    else:
        st.error("Please enter a valid amount!")

# Display transaction history
st.header("Transaction History")
if not st.session_state.data.empty:
    st.dataframe(st.session_state.data)

    # Summary metrics
    income = st.session_state.data[st.session_state.data["Type"] == "Income"]["Amount"].sum()
    expenses = st.session_state.data[st.session_state.data["Type"] == "Expense"]["Amount"].sum()
    balance = income - expenses

    st.subheader("Summary")
    st.metric("Total Income", f"${income:.2f}")
    st.metric("Total Expenses", f"${expenses:.2f}")
    st.metric("Current Balance", f"${balance:.2f}")

    # Visualization
    st.header("Spending Analysis")
    expense_data = st.session_state.data[st.session_state.data["Type"] == "Expense"]
    if not expense_data.empty:
        fig = px.pie(expense_data, names="Category", values="Amount", title="Expenses by Category")
        st.plotly_chart(fig)
else:
    st.info("No transactions added yet!")

