'''
Basicos 4
En este script se muestra como crear inputs de fecha, hora y color en Streamlit.
'''

import streamlit as st
from datetime import date



def inputFecha():
    # Establecer la fecha mínima y máxima
    fecha_minima = date(1940, 1, 1)
    fecha_maxima = date(2003, 1, 1)
    # Crear el input de fecha
    cita = st.date_input(
        "Selecciona una fecha",
        min_value=fecha_minima,  # Fecha máxima permitida
        max_value=fecha_maxima,  # Fecha mínima permitida
    )

    st.write(f"La fecha seleccionada es: {cita}")

def inputHora():
    from datetime import time, datetime

    # Establecer una hora predeterminada y un rango de horas
    hora_predeterminada = time(12, 0)  # 12:00 PM
    hora_minima = time(9, 0)  # 9:00 AM
    hora_maxima = time(18, 0)  # 6:00 PM

    # Crear el input de hora
    hora = st.time_input(
        "Selecciona una hora (entre 9:00 AM y 6:00 PM)",
        value=hora_predeterminada,
        min_value=hora_minima,
        max_value=hora_maxima,
        step=1800  # Intervalo de 30 minutos
    )

    # Mostrar la hora seleccionada en formato de 12 horas
    hora_formato_12 = hora.strftime("%I:%M %p")
    st.write(f"La hora seleccionada es: {hora_formato_12}")


def main():
    st.set_page_config(page_title="Eres mi perra", page_icon=":smiley:")
    st.title("Welcome to My Streamlit App")
    nombre =st.text_input("Escribe tu nombre aqui")#coloca un input
    st.write(f"Hello {nombre}")

    area = st.text_area("Escribe algo aqui", height=100)#coloca un area de texto
    st.write(f"Esto es lo que escribiste: {area}")

    numeros = st.number_input("Escribe un numero", min_value=0, max_value=100, step=1)#coloca un input de numeros
    st.write(f"El numero que escribiste es: {numeros}")

    cita = st.date_input("Selecciona una fecha")#coloca un input de fecha
    st.write(f"La fecha seleccionada es: {cita}")
    inputFecha()#Aqui se muestra como poner minimo y maximo a la fecha

    hora = st.time_input("Selecciona una hora")#coloca un input de hora
    st.write(f"La hora seleccionada es: {hora}")

    color = st.color_picker("Selecciona un color")#coloca un input de color
    st.write(f"El color seleccionado es: {color}")


if __name__ == "__main__":
    main()