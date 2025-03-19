import streamlit as st
import pandas as pd
import plotly.express as px
import os

csv_file = "vehicles_us.csv"

if not os.path.exists(csv_file):
    st.error(f"❌ Archivo '{csv_file}' no encontrado. Asegúrate de que está en la carpeta correcta.")
else:
    car_data = pd.read_csv(csv_file)

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

    st.write("🚀 La aplicación ha iniciado correctamente.")
    