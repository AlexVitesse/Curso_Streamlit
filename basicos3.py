'''
Basicos 3
En este script se muestra como mostrar imagenes, videos y audios en Streamlit.
Tambien se muestra como incrustar videos de YouTube en Streamlit.

'''
import streamlit as st
from PIL import Image

def youtubeVideo():
    # URL del video de YouTube
    url_youtube = "https://www.youtube.com/watch?v=ngbvguu1Zzs"

    # Incrustar el video usando HTML
    st.markdown(f"""
    <iframe width="560" height="315" src="{url_youtube.replace('watch?v=', 'embed/')}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, unsafe_allow_html=True)

def videoUrl():#Muestra un video de una url NO RECOMENDADO PARA YOUTUBE
    # Enlace directo a un archivo de video (no es un enlace de YouTube)
    url_video = "https://www.w3schools.com/html/mov_bbb.mp4"

    # Mostrar el video
    st.video(url_video)

def incrustarVideo():
    from streamlit.components.v1 import html

    # URL del video de YouTube
    url_youtube = "https://www.youtube.com/watch?v=ngbvguu1Zzs"  # Cambia esto por la URL de tu video

    # Crear el código HTML para el video
    video_html = f"""
    <iframe width="560" height="315" src="{url_youtube.replace('watch?v=', 'embed/')}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """

    # Incrustar el video usando components.html
    html(video_html, width=560, height=315)


def main():
    st.title("Welcome to My Streamlit App Media")
    #img = Image.open("Sources/imagen1.jpg")  
    #Asi se coloca una imagen.
    #st.image(img, caption="El mismismo deepseek", use_column_width=True)#asi era antes
    #st.image(img, caption="El mismismo deepseek", use_container_width=True)#Asi es ahora
    #st.image("https://picsum.photos/800") #asi se puede poner una imagen de internet
    #Asi se puede poner un video
    #with open("Sources/video.mp4", "rb") as file:
        #st.video(file.read(), start_time=0)    #start_time es el tiempo en el que empieza el video
    #Asi se puede poner un audio
    with open("Sources/music.mp3", "rb") as music:
        st.audio(music.read(), start_time=0)
    youtubeVideo()
    videoUrl()
    incrustarVideo()
    
if __name__ == "__main__":
    main()