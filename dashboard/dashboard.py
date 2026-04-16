import streamlit as st
import pandas as pd

st.set_page_config(page_title = "E-Commerce Analysis Dashboard", layout = "wide")
st.title ( "E-Commerce Analysis Dashboard")

df = pd.read_csv("dashboard/main_data.csv")
df['order_purchase_timestamp'] = pd.to_datetime(df["order_purchase_timestamp"])

st.subheader("Input Your Date")

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()
              
date_range = st.sidebar.date_input(
    "Choose Range Date",
    value=(min_date, max_date),
    min_value = min_date,
    max_value = max_date
)


if len(date_range) ==2:
    start_date, end_date = date_range

else :
    start_date, end_date = min_date, max_date


filtered_df = df[
    (df["order_purchase_timestamp"].dt.date >= start_date) &
    (df["order_purchase_timestamp"].dt.date >= end_date) 
]

st.subheader("Analysis Result")

col1, col2 = st.columns(2)

with col1 :
    st.metric("Total Orders", len(filtered_df))

with col2 : 
    st.metric("Top 10 Cities", filtered_df['customer_city'].nunique())


st.subheader("Monthly Order Trends")

if not filtered_df.empty:
    filtered_df["month"] = filtered_df["order_purchase_timestamp"].dt.to_period("M").astype(str)
    monthly_orders = filtered_df.groupby("month").size()
    st.line_chart(monthly_orders)
else:
    st.warning("Tidak ada data pada filter yang dipilih.")

st.subheader("Top 10 Cities")

top_city = df['customer_city'].value_counts().head(10)
st.bar_chart(top_city)

