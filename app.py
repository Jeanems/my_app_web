import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")  # Asegúrate de que el archivo esté en la misma carpeta

st.title("🚗 Analizador de vehículos en venta")

st.write("Esta aplicación permite visualizar datos de anuncios de venta de autos en EE.UU.")

if st.checkbox("Mostrar histograma del odómetro"):
    st.write("📊 Histograma del odómetro (millas recorridas)")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar gráfico de dispersión entre precio y odómetro"):
    st.write("📈 Relación entre el precio y el odómetro")
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)
    
import streamlit as st
st.write("🚀 La aplicación ha iniciado correctamente.")