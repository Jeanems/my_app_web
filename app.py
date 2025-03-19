import streamlit as st
import pandas as pd
import plotly.express as px
import os

car_data = pd.read_csv("vehicles_us.csv")

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

if __name__ == "__main__":
 import streamlit.web.cli as stcli
 import sys
 port = int(os.environ.get("PORT", 8501))
 sys.argv = ["streamlit", "run", "app.py", "--server.port", str(port)]
 stcli.main()
 