import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.header('Market of used cars.Original data')
st.write ('Filter the data below to see the ads by manufacturer')


df = pd.read_csv('vehicles_us.csv')
df = df.drop(df.columns[0], axis=1)


manufacturer = df['manufacturer_name'].unique() 

select_manufacturer = st.selectbox('Select a Manufacturer', manufacturer)

df_filtered = df[ df.manufacturer_name == selected_manufacturer ]

df_filtered