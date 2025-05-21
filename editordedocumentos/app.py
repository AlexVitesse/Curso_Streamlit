import streamlit as st
import pandas as pd
import time

ruta = "C:/Users/pcdec/OneDrive/Documentos/Python/CURSO STREAMLIT/Sources/Pokemon_Cards.csv"
def cargarArchivo(archivo_datos):
    df = pd.read_csv(archivo_datos, encoding='UTF-8')  # Asegúrate de que el archivo esté en la misma carpeta o proporciona la ruta completa.
    return df

def main():
    st.title("Editor de codigo")
    st.write("Sube tu archivo CSV para editarlo, guardar y descargar")
    #Cargar archivo
    archivo_datos = st.file_uploader("Cargar archivo CSV", type=["csv"])

    if archivo_datos is not None:
        with st.form("Formulario_edicion"):
            df = cargarArchivo(archivo_datos)
            df_editado = st.data_editor(df)
            boton_guardar = st.form_submit_button("Guardar")
        if boton_guardar:
            marca_tiempo = time.strftime("%Y%m%d-%H%M%S")
            nombre_archivo = f"{archivo_datos.name.split('.')[0]}_{marca_tiempo}.csv"
            df_final = df_editado.to_csv(index=False, encoding='UTF-8')
            st.download_button(
                "Descargar archivo", 
                data=df_final, 
                file_name=nombre_archivo, 
                mime="text/csv"
            )
            st.success("Archivo guardado y listo para descargar")
            
if __name__ == "__main__":
    st.set_page_config(page_title="Editor de codigo", page_icon="📊", layout="wide")
    main()
