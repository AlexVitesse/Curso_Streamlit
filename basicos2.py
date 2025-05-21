'''
# Importar las librerias necesarias para el proyecto son streamlit (panda viene por defecto en streamlit)
pip install streamlit
En este hay como manejar datadframes, selectbox, multiselect, slider, select_slider.

'''
import streamlit as st
import pandas as pd

df = pd.read_csv('pokemon.csv')
#df2 = df.sample(n=1000, random_state=42)

def main():
    st.title("Curso de Streamlit")  #Asi se pone un titulo
    #st.header("Dataframe")
    #st.dataframe(df)  #Asi se muestra un dataframe
    #st.table(df)  #Asi se muestra un dataframe PERO ME MUESTRA TODA LA TABLA. NO SE RECOMIENDA.
    #st.dataframe(df2.style.highlight_max(axis=0))  #Asi se muestra un dataframe con el maximo valor resaltado
    #st.write(df.head())  #Asi se muestra un dataframe con solo los primeros 5 valores
    #st.json(df.head().to_json())  #Asi se muestra un dataframe en formato json
    #st.json({"Clave": "Valor"})  #Asi se muestra un json personalizado
    #code = """
    #def hello():
    #    print("Hello, Streamlit!")
    #"""
    #st.code(code, language='python')  #Asi se muestra un codigo en python
    opcion = st.selectbox(  #Asi se muestra un selectbox
        'Elige tu pokemon favorito:',
        ['Pikachu', 'Charmander', 'Bulbasaur']#El primero sera el valor por defecto.
    )
    st.write(f'Elegiste a {opcion} como tu pokemon favorito')

    opciones = st.multiselect(  #Asi se muestra un multiselect para varias opciones
        'Elige tu pokemon favorito:',
        ['Pikachu', 'Charmander', 'Bulbasaur']
    )
    st.write(f'Elegiste a {opciones} como tu pokemon favorito')

    #Slider
    edad = st.slider(#Muestra una barra para seleccionar un valor con un rango pero numerico
        '¿Cuál es tu edad?',
        min_value=0,
        max_value=100,
        value=25, #Valor por defecto
        step=1  #Incremento
    )
    st.write(f'Tu edad es {edad} años')
    #Select Slider
    nivel = st.select_slider(#Muestra una barra para seleccionar un valor con un rango pero de palabras
        '¿Selecciona una dificultad?',
        options=['Bajo', 'Medio', 'Alto'],
        value='Medio', #Valor por defecto
    )
    st.write(f'Tu edad es {nivel} años')




if __name__ == "__main__":
    main() 