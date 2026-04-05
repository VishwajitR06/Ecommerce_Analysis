import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title("📦 E-Commerce Sales Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

    # Show raw data
    st.subheader("Raw Data")
    st.write(df.head())

    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Basic summary
    st.subheader("Summary")
    st.write(df.describe())

    # Total Quantity by Country
    st.subheader("Total Quantity Sold by Country")
    country_quantity = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    country_quantity.plot(kind='bar', ax=ax)
    ax.set_ylabel("Total Quantity Sold")
    ax.set_title("Quantity Sold by Country")
    st.pyplot(fig)

    # Add filter for specific country
    st.subheader("Country-wise Invoice Explorer")
    country = st.selectbox("Select a Country", df["Country"].unique())
    st.dataframe(df[df["Country"] == country])

else:
    st.warning("Please upload a CSV file to continue.")
