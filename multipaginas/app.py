import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Pagina principal")
    st.write("Bienvenido a la página principal de la aplicación.")
    st.write("Usa el menu de la izquierda para navegar entre las diferentes páginas.")

def visualizacion_datos():
    st.title("Visualización de datos")
    st.write("Carga un archivo CSV para visualizar los datos.")
    archivo_cargado = st.file_uploader("Cargar archivo CSV", type=["csv"])
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos cargados:")
        st.write(df)
        st.write("Estadisticas descriptivas")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Graficos interactivos")
    st.write("Crea graficos interactivos con los datos cargados.")
    archivo_cargado = st.file_uploader("Cargar archivo CSV", type=["csv"], key=2)
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columa para el EJE X")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elige una columa para el EJE Y")
        eje_y = st.selectbox("Eje Y", df.columns)

        if st.button("Crear grafico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_x} por {eje_y}")
            st.plotly_chart(fig)
        

st.sidebar.title("Navegacion")
pagina = st.sidebar.selectbox(
    "Selecciona una opcion",
    ["Pagina principal","Visualizacion de datos",
    "Graficos interactivos"]
)



match pagina:
    case "Pagina principal":
        main()
    case "Visualizacion de datos":
        visualizacion_datos()
    case "Graficos interactivos":
        graficos_interactivos()

