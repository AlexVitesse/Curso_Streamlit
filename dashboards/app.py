import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

ruta1 = "Sources/pokemon.csv"
ruta2 = "Sources/bitcoin_dataset.csv"

#Configuracion de la pagina
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Dashboard")
st.markdown("## Explorando diferentes bibliotecas de visualización de python")

#1. Introduccion
with st.expander("Introducción", expanded=True):
    st.markdown(""" 
    Esta aplicación web está diseñada para explorar diferentes bibliotecas de visualización de Python. A continuación, se presentan algunas de las bibliotecas más populares y sus características principales:
    * **Matplotlib**: Es una de las bibliotecas más antiguas y ampliamente utilizadas para la visualización de datos en Python. Es altamente personalizable y flexible, pero puede requerir más código para crear gráficos complejos.
    * **Seaborn**: Basada en Matplotlib, Seaborn proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos y informativos. Es especialmente útil para explorar y visualizar datos estadísticos.
    * **Plotly**: Es una biblioteca interactiva que permite crear gráficos interactivos y animados. Es especialmente útil para aplicaciones web y dashboards.
    * **Streamlit**: Es una biblioteca de Python que permite crear aplicaciones web interactivas con muy poco código. Es ideal para prototipar y desplegar aplicaciones de visualización de datos rápidamente.
    
    """)

try:
    pokemon_df = pd.read_csv(ruta1)
    bitcoin_df = pd.read_csv(ruta2) 
    st.success("Los datos se cargaron correctamente")

    #3. Visualizacion con Matplotlib
    st.header("Visualización con Matplotlib")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gráfico de dispersión")
            fig, ax = plt.subplots(figsize=(8, 6))
            nombres = pokemon_df['Name'].head(5)
            ataque = pokemon_df['Attack'].head(5) 
            ax.scatter(nombres, ataque, color='blue', alpha=0.6)
            plt.xticks(rotation=45)
            plt.title('Ataque de los primeros 5 Pokémon')
            plt.xlabel('Nombre del Pokémon')
            plt.ylabel('Ataque')
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("Grafico de barras")
            fig, ax = plt.subplots(figsize=(8, 6))
            nombres = pokemon_df['Name'].head(5)
            ataque = pokemon_df['Attack'].head(5) 
            ax.bar(nombres, ataque, color='skyblue', alpha=0.6)
            plt.xticks(rotation=45)
            plt.title('Ataque de los primeros 5 Pokémon')
            plt.xlabel('Nombre del Pokémon')
            plt.ylabel('Ataque')
            st.pyplot(fig)
            plt.close()

    #4. Visualizacion con Seaborn
    st.header("Visualización con Seaborn")
    with st.container():
        col1, col2 = st.columns(2)
        diezPrimeros = bitcoin_df.head(20)
        with col1:
            st.subheader("Grafico de violin")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.violinplot(data =diezPrimeros, x = 'Date', y = 'btc_market_price')
            plt.xticks(rotation=45)
            plt.title('Precio del Bitcoin')
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("Grafico de violin")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxenplot(data =diezPrimeros, x = 'Date', y = 'btc_market_price')
            plt.xticks(rotation=45)
            plt.title('Precio del Bitcoin')
            st.pyplot(fig)
            plt.close()
    

    #5. Visualizacion con Plotly
    st.header("Visualización interactiva con Plotly")
    with st.container():
        #Grafico de linea interactico
        fig = px.line(
            diezPrimeros,
            x='Date', 
            y='btc_market_price', 
            title='Precio del Bitcoin', 
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)

        #Grafico de pastel o torta
        fig = px.pie(bitcoin_df, values='btc_market_price', names='Date', title='Distribución del precio del Bitcoin')
        st.plotly_chart(fig, use_container_width=True)

    #6. Seccion interactiva
    st.header("🚬🗿Sección interactiva")
    dataset_choice = st.radio(
        "Selecciona el conjunto de datos",
        ["Pokemon", "Bitcoin"]
    )
    if dataset_choice == "Pokemon":
        df = pokemon_df
    else:
        df = bitcoin_df
    #Selector de visualizacion
    chart_type = st.selectbox(
        "Selecciona el tipo de gráfico", 
        ["Barras", "Dispersion", "Linea"]
    )
    #Selector de datos
    x_axis = st.selectbox("Selecciona el eje X", df.columns)
    y_axis = st.selectbox("Selecciona el eje Y", df.columns)
     
    #Generar el grafico seleccionado
    match chart_type:
        case "Barras":
            fig = px.bar(df, x=x_axis, y=y_axis)
        case "Dispersion":
            fig = px.scatter(df, x=x_axis, y=y_axis)
        case "Linea":
            fig = px.line(df, x=x_axis, y=y_axis)
    st.plotly_chart(fig, use_container_width=True)                         
    
except Exception as e:
    st.error(f"Error al cargar el archivo: {e}")