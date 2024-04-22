import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.header('Market of used cars.Original data')
st.write('Filter the data below to see the listings by manufacturer')

df = pd.read_csv('vehicles_us.csv')



def extract_manufacturer_model(model):
    if pd.isnull(model):
        return None, None
    else:
        manufacturer_model = model.split(' ', 1)
        if len(manufacturer_model) == 1:
            return manufacturer_model[0], None
        else:
            return manufacturer_model


df['manufacturer'], df['model'] = zip(*df['model'].apply(extract_manufacturer_model))


df['is_4wd'].fillna(0, inplace=True)
df['paint_color'].fillna('unknown', inplace=True)

manufacturer_choice = ['all'] + list(df['manufacturer'].unique())

selected_manufacturer = st.selectbox('Select a manufacturer', manufacturer_choice )


if selected_manufacturer == 'all':
    df_filtered = df
else:
    
    df_filtered = df[df['manufacturer'] == selected_manufacturer]
    

model_choice = ['all'] + list(df_filtered['model'].unique())

selected_model = st.selectbox('Select a model', model_choice)


if selected_model != 'all':
    df_filtered = df_filtered[df_filtered['model'] == selected_model]

min_year, max_year = int(df_filtered['model_year'].min()), int(df_filtered['model_year'].max())

year_range = st.slider("Choose years", value=(min_year, max_year), min_value=min_year,max_value= max_year)

actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df_filtered[df_filtered['model_year'].isin(actual_range)]
df_filtered



vehicle_types = ['All'] + list(df['type'].unique())


st.header("Scatter Plot of Price by Vehicle Type")
selected_type = st.selectbox("Select a vehicle type", vehicle_types)


if selected_type == 'All':
    filtered_df = df
else:
    filtered_df = df[df['type'] == selected_type]


fig = px.scatter(filtered_df, x='price', y=filtered_df.index, title=f'Price Scatter Plot for {selected_type}s',
                 labels={'price': 'Price', 'index': 'Index'})
st.plotly_chart(fig)