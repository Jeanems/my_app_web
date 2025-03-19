import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis de Vehículos en EE.UU.")

hist_button = st.button('Construir histograma')

if hist_button:
    fig = px.histogram(car_data, x="price")  # Ajusta la columna según tu dataset
    st.plotly_chart(fig)