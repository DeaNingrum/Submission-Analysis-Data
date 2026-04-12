import streamlit as st
import pandas as pd

st.title ( "Dashboard Analisis E-Commerce")

df = pd.read_csv("dashboard/main_data.csv")
df['order_purchase_timestamp'] = pd.to_datetime(df["order_purchase_timestamp"])

st.subheader("Hasil Analisis Data")

col1, col2 = st.columns(2)

with col1 :
    st.metric("Total order", len(df))

with col2 : 
    st.metric("10 Kota Teratas", df['customer_city'].nunique())


st.subheader("Tren Order Bulanan")

df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
monthly_orders = df.groupby('month').size()

st.line_chart(monthly_orders)   

st.subheader("Top 10 Kota")

top_city = df['customer_city'].value_counts().head(10)
st.bar_chart(top_city)