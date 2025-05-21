import streamlit as st
import pandas as pd
from pokedex import cargarPokemones
from texto import appTexto


def main():
    st.title("App vergas")
    menu  = ["Home", "Pokemon","Texto","Conocenos"]
    eleccion = st.sidebar.selectbox("Menu", menu)
    match eleccion:
        case "Home":
            st.subheader("Bienvenido a la pagina de inicio")
        case "Pokemon":
            cargarPokemones()
        case "Texto":
            appTexto()
        case "Conocenos":
            st.subheader("Conocenos")
        

if __name__ == "__main__":
    main()