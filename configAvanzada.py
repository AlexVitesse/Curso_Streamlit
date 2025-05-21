#Autor: Eric Vazquez 
#En este se configura la pagina de streamlit con un logo y se agrega un grafico 
# de pastel y de barras
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd


img = Image.open("Sources/logo.png")
st.set_page_config(page_title="Condor Assistent", page_icon=img, layout="wide",
                   initial_sidebar_state="collapsed")


def cargarPokemones():
    df = pd.read_csv("Sources/Pokemon_Cards.csv")
    # Filtrar el DataFrame
    # Cuadro de selección para buscar
    nombres = df["Name"].unique()
    seleccion = st.selectbox("Selecciona un nombre:", nombres)
    # Filtrar el DataFrame
    resultado = df[df["Name"] == seleccion]
    impresion = resultado["Image"].values[0]
    st.image(impresion, width=300)

    # Mostrar el resultado
    st.write(f"Resultados para '{seleccion}':")
    st.dataframe(resultado)

def main():
    st.title("Welcome to My Streamlit App!")
    st.sidebar.header("Navegacion")
    df = pd.read_csv("Sources/Pokemon_Cards.csv")
    cargarPokemones()
    st.dataframe(df)
    df_count = df.groupby("Type").count().reset_index()
    fig = px.pie(df_count, values="Name", names="Type", title="Pokemon Types")
    st.plotly_chart(fig)
    #COMO SACAR MEDIA CON BARRAS no sirve si el valor no es numerico.
    df_avg = df.groupby('Set')["Type"].mean().reset_index()#Sirve para hacer la media pero no funciona si no son valores numericos
    fig2 = px.bar(df_avg, x="Set", y="Type", title="Media de Tipos por Set")
    #st.plotly_chart(fig2)



if __name__ == "__main__":
    main()

