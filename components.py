import streamlit as st
from streamlit.components.v1 import html

def insertarHTML():

    # Código HTML personalizado
    html_code = """
    <h1 style="color: blue;">¡Hola, Streamlit!</h1>
    <p>Este es un <strong>texto en negrita</strong>.</p>
    <button onclick="alert('Hiciste clic!')">Haz clic aquí</button>
    """

    # Incrustar el HTML en la app
    html(html_code, width=300, height=150)

def insertarIframe():
    # Código HTML para un iframe de Google Maps
    iframe_code = """
    <iframe
        width="600"
        height="450"
        style="border:0"
        loading="lazy"
        allowfullscreen
        src="https://www.google.com/maps/embed/v1/place?key=TU_API_KEY&q=Eiffel+Tower,Paris+France">
    </iframe>
    """

    # Incrustar el iframe en la app
    html(iframe_code, width=600, height=450)

def incustrarGraficos():
    # Código HTML con D3.js
    d3_code = """
    <div id="chart"></div>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script>
        var data = [30, 86, 168, 281, 303, 365];
        d3.select("#chart")
        .selectAll("div")
        .data(data)
        .enter()
        .append("div")
        .style("width", function(d) { return d + "px"; })
        .text(function(d) { return d; });
    </script>
    """

    # Incrustar el gráfico en la app
    html(d3_code, width=400, height=200)

def incrustarReproductor():
    # Código HTML para un reproductor de audio
    audio_code = """
    <audio controls>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        Tu navegador no soporta la reproducción de audio.
    </audio>
    """

    # Incrustar el reproductor de audio en la app
    html(audio_code)

def main():
    st.set_page_config(page_title="Componentes Examples", page_icon="🦅", layout="wide")
    st.title("Componentes HTML en Streamlit")
    #insertarHTML()
    #insertarIframe()#Requiere una key de google maps
    #incustrarGraficos()#NO FUNCIONA
    incrustarReproductor()

if __name__ == "__main__":
    main()