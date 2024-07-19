
import streamlit as st  #Librería para visualizar la aplicación web
import pandas as pd
import plotly.express as px   #Librería para creación de gráficos

# Para correr streamlit se corre en terminal el comando: streamlit run app.py

def pagina_principal():
    st.title("Página Principal")
    st.write("¡Bienvenido a la aplicación de demostración!")
    st.write("usa el menú de la izquierda para navegar entre las páginas")

def visualizar_datos():
    st.title("Visualización de Datos")
    st.write("Carga un archivo CSV para visualizar los datos")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv")

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo CSV:")
        st.write(df)
        st.write("Estadísticas descriptivas:")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Gráficos Interactivos")
    st.write("Carga un archivo CSV para crear gráficos interactivos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columna para el eje X:")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elige una columna para el eje Y:")
        eje_y = st.selectbox("Eje Y", df.columns)

        if st.button("Crear Gráfico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)


st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", "Visualización de Datos", "Gráficos Interactivos"])

if pagina == "Página Principal":
    pagina_principal()
elif pagina == "Visualización de Datos":
    visualizar_datos()
elif pagina == "Gráficos Interactivos":
    graficos_interactivos()
