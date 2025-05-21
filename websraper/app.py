import os
import re
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

def get_product_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "es-ES,es;q=0.9"
    }
    
    response = requests.get(url, headers=headers) 
    soup = BeautifulSoup(response.content, features='lxml') 
    try:
        title = soup.find(id="productTitle").get_text(strip=True)
    except Exception as e:
        title = 'No se pudo obtener el título'  # Manejo de errores en caso de que no se encuentre el título.
    
    try:
        image_url = soup.find(id="landingImage")['src']  # Obtener la URL de la imagen.
    except Exception as e:
        image_url = None
    
    try:
        price = soup.find('span', {'class': 'a-offscreen'}).get_text(strip=True)
        if "Página" in price:
            price = "Agotado"
    except Exception as e:
        price = 'No se encontró precio'  # Manejo de errores en caso de que no se encuentre el precio.

    return title, image_url, price

def save_image(image_url, title):  # Función para guardar la imagen.
    folder  = "imagenes"
    os.makedirs(folder, exist_ok=True)  # Crear la carpeta si no existe.

    valid_filename = re.sub(r'[<>:"/\\|?*]', '', title)  # Limpiar el título para usarlo como nombre de archivo.
    valid_filename = valid_filename[:10]    # Limitar el nombre del archivo a 10 caracteres.
    filepath = os.path.join(folder, valid_filename + '.jpg')

    # Ensure the filename is unique to avoid permission issues
    base, ext = os.path.splitext(filepath)
    counter = 1
    while os.path.exists(filepath):  # Si el archivo ya existe, agregar un número al nombre.
        filepath = f"{base}_{counter}{ext}"
        counter += 1
    
    response = requests.get(image_url, stream=True)  # Descargar la imagen.
    if response.status_code == 200:  # Si la descarga fue exitosa, guardar la imagen.
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):  # Guardar la imagen en trozos de 1024 bytes.
                file.write(chunk)
        return filepath
    return None

def save_to_excel(data):
    df = pd.DataFrame(data)
    file_name = f"busquedas.xlsx"  # Nombre del archivo Excel.

    if os.path.exists(file_name):  # Si el archivo ya existe, abrirlo y agregar los nuevos datos.
        existing_df = pd.read_excel(file_name)  # Leer el archivo existente.
        df = pd.concat([existing_df, df], ignore_index=True)  # Concatenar los datos existentes con los nuevos.
    
    df.to_excel(file_name, index=False)  # Guardar los datos en el archivo Excel.
    return file_name

def get_search_results(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.com/",
        "DNT": "1"
    }
    url = f"https://www.amazon.com/s?k={query}"
    #print("El url en get_search_results es: ", url)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción si la solicitud no fue exitosa.
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los resultados de búsqueda: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    #print("Si tengo respuesta del url")

    product_links = []
    try:
        # Buscar todos los enlaces que coincidan con la clase actual.
        for link in soup.find_all('a', attrs={"class": 'a-link-normal s-no-outline'}, href=True):
            if not link["href"].startswith("/"):
                link["href"] = "/" + link["href"]
            product_links.append("https://www.amazon.com" + link["href"])
    except Exception as e:
        print(f"Error al analizar los resultados de búsqueda: {e}")
    
    return product_links

# Streamlit app
st.title("Búsqueda de productos en Amazon")
search_query = st.text_input("Ingrese su búsqueda:")

if search_query:
    st.write(f"Resultados para: {search_query}")
    search_query = search_query.replace(" ", "+")

    # Spinner para la búsqueda de productos
    with st.spinner("Buscando productos..."):
        product_links = get_search_results(search_query)  # Obtener los enlaces de los productos.

    if product_links:
        all_data = []  # Lista para almacenar los datos de todos los productos.
        for url in product_links[:10]:  # Limitar a los primeros 10 productos para evitar sobrecargar la API.
            # Spinner para la obtención de detalles del producto
            with st.spinner(f"Obteniendo detalles del producto {len(all_data) + 1}..."):
                title, image_url, price = get_product_info(url)   # Obtener los datos del producto.

            if title != "No se pudo obtener el título":
                data = {
                    'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Agregar la fecha y hora actual.
                    'Título': title,
                    'Precio': price,
                    'URL de la imagen': image_url,
                    'URL del producto': url
                }
                all_data.append(data)  # Agregar los datos a la lista.
                if image_url:
                    save_image(image_url, title)  # Guardar la imagen.

        if all_data:
            df = pd.DataFrame(all_data)  # Crear un DataFrame con los datos.
            st.write("### Información de los productos")
            st.dataframe(df.style.set_properties(**{'text-align': 'left'}))  # Mostrar el DataFrame.
            
            # Guardar los datos en el Excel
            file_name = save_to_excel(all_data)  # Guardar los datos en un archivo Excel.
            st.success(f"Datos guardados en {file_name}")  # Mostrar un mensaje de éxito.
        else:
            st.error("No se encontraron productos válidos.")
    else:
        st.error("No se encontraron resultados para la búsqueda.")