import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Vehículos en Venta')

# Carga del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    # Mostrar mensaje informativo
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma con Plotly Express
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:  # Si la casilla de verificación está seleccionada
    # Mostrar mensaje informativo
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        title="Relación entre Odómetro y Precio",
        labels={"odometer": "Kilometraje", "price": "Precio (USD)"},
        color="condition"  # Colorea los puntos según la condición del coche
    )
    
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
