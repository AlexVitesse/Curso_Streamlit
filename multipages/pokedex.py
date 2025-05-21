import streamlit as st
import pandas as pd

def cargarPokemones():
    st.subheader("Pokedex:")
    ruta = "C:/Users/pcdec/OneDrive/Documentos/Python/CURSO STREAMLIT/Sources"
    df = pd.read_csv(ruta + "/Pokemon_Cards.csv")
    st.dataframe(df)


