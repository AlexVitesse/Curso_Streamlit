import streamlit as st

def main():
    st.title("Curso de Streamlit")  #Asi se pone un titulo 
    st.header("Esto es un encabezado")  #Asi se pone un encabezado
    st.subheader("Esto es un subencabezado") #Asi se pone un subencabezado
    st.text("Esto es un texto") #Asi se pone un texto
    nombre = "Alejandro"
    st.text(f"Esto es un texto con formato {nombre}")   #Asi se pone un texto con formato
    st.markdown("# Esto es un markdown") #Asi se pone un markdown
    
    #Markdown es un lenguaje de marcado ligero que se utiliza para dar formato a textos de manera 
    #sencilla. En Streamlit, puedes usar Markdown para agregar texto formateado a tus 
    #aplicaciones web, como títulos, subtítulos, listas, enlaces, negritas, cursivas, y más.
    st.markdown("# ¡Hola, Streamlit! 👋")
    st.markdown("## Esto es un subtítulo")
    st.markdown("**Texto en negrita** y *texto en cursiva*.")
    st.markdown("- Elemento 1")
    st.markdown("- Elemento 2")
    st.markdown("[Visita Streamlit](https://streamlit.io)")
    st.markdown("```python\nprint('Código en Streamlit')\n```")
    
    #Mensajes para el usuario.
    st.success("¡Éxito!") #Asi se pone un mensaje de exito
    st.warning("¡Advertencia!") #Asi se pone un mensaje de advertencia
    st.info("¡Información!") #Asi se pone un mensaje de información 
    st.error("¡Error!") #Asi se pone un mensaje de error
    st.exception("¡Excepción!") #Asi se pone un mensaje de excepción
    st.write("Esto es un texto") #Asi se pone un texto
    st.write(1+1) #Asi se pone una operación

if __name__ == "__main__":
    main()
