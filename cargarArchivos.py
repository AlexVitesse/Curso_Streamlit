import streamlit as st
import pandas as pd
from PIL import Image
import docx2txt as docx
from PyPDF2 import PdfReader
import os

@st.cache_data #Esto guarda en cache la imagen.
def cargarImagen(Imagen):
    img = Image.open(Imagen)
    return img

def cargarArchivo(archivo):
    try:
        pdf = PdfReader(archivo)
        count = len(pdf.pages)
        todoElTexto = ""
        for i in range(count):
            page = pdf.pages[i]
            texto = page.extract_text()
            if texto:  # Verificar si se extrajo texto
                todoElTexto += texto
        return todoElTexto if todoElTexto else "No se pudo extraer texto del PDF."
    except Exception as e:
        return f"Error al extraer texto del PDF: {e}"

def guardarArchivo(archivo):
    #guardar el archivo y crea la ruta sino existe.
    if not os.path.exists("tempDir"):
        os.mkdir("temp")
    with open(os.path.join("temp",archivo.name),"wb") as f:
        f.write(archivo.getbuffer())
    return st.success("Archivo Guardado {}".format(archivo.name))

def main():
    st.set_page_config(page_title="Archivos", page_icon=":open_file_folder:")
    st.title("Cargar Archivos")
    menu = ["Imagen","Conjunto de datos", "Archivos de documentos"]
    eleccion = st.sidebar.selectbox("Menu", menu)
    match eleccion:
        case "Imagen":
            st.subheader("Cargar imagenes")
            archivo_imagen = st.file_uploader("Cargar imagen", type=["png","jpg","jpeg"])#Con esto se cargan imagenes
            if archivo_imagen is not None:
                detalles_imagen = {"Nombre":archivo_imagen.name, "Tipo":archivo_imagen.type, "Tamaño":archivo_imagen.size}
                st.write(detalles_imagen)
                st.image(cargarImagen(archivo_imagen), width=500)
                guardarArchivo(archivo_imagen) #Con esto se guarda el archivo 

        case "Conjunto de datos":
            st.subheader("Cargar conjunto de datos")
            archivo_datos = st.file_uploader("Cargar archivo csv o excel", type=["csv","xlsx"])#Con esto se cargan archivos de datos
            if archivo_datos is not None:
                detalles_datos = {"Nombre":archivo_datos.name, "Tipo":archivo_datos.type, "Tamaño":archivo_datos.size}
                st.write(detalles_datos)
                if detalles_datos["Tipo"] == "text/csv":
                    df = pd.read_csv(archivo_datos)
                elif detalles_datos["Tipo"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    df = pd.read_excel(archivo_datos)
                else:
                    print("Es un formato no compatible")
                    df = pd.DataFrame()
                st.dataframe(df)
                guardarArchivo(archivo_datos) #Con esto se guarda el archivo
        case "Archivos de documentos":
            st.subheader("Cargar archivos de documentos")
            archivo_documento = st.file_uploader("Cargar archivo de documento PDF, DOCX o TXT", type=["pdf","docx","txt"])#Con esto se cargan archivos de documentos
            if st.button("Procesar"):
                if archivo_documento is not None:
                    detalles_documento = {"Nombre":archivo_documento.name, "Tipo":archivo_documento.type, "Tamaño":archivo_documento.size}
                    st.write(detalles_documento)
                    if detalles_documento["Tipo"] == "application/pdf":
                        texto = cargarArchivo(archivo_documento)
                    elif detalles_documento["Tipo"] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        texto = docx.process(archivo_documento)
                    else:
                        #texto = str(archivo_documento.read(),"utf-8")
                        texto = archivo_documento.getvalue().decode("utf-8")  # `read()` puede vaciar el buffer, mejor usar `getvalue()`
                    st.write(texto)
                    guardarArchivo(archivo_documento) #Con esto se guarda el archivo

        case _:
            print("Seleccione una opción")

if __name__ == "__main__":
    main()
