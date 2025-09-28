import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers interactively")

df = pd.read_csv('metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

year_range = st.slider("Select year range", 2019, 2023, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]


st.dataframe(filtered_df.head())

year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)
