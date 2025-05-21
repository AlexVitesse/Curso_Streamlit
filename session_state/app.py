import streamlit as st
def home_page():
    st.subheader("Pagina de Inicio")
    if "contador" not in st.session_state:
        st.session_state.contador = 0
    
    def incrementar_contador():
        st.session_state.contador *=1
    def decrementar_contador():
        st.session_state.contador -=1
    
    st.write("El calor del contador es:", st.session_state.contador)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("incrementar", on_click=incrementar_contador)
    with col2:
        st.button("Decrementar", on_click=decrementar_contador)


def settings_page():
    st.subheader("Pagina de Configuracion")
    if "size" not in st.session_state:
        st.session_state.size = 20
    
    def incrementar_contador():
        st.session_state.size *=1
    def decrementar_contador():
        st.session_state.size -=1
    st.write(f"Tamaño de la fuente actual: {st.session_state.size}")

    texto_html = f""""
       <p style="font-size: {st.session_state.size}px;">
       Este es un texto de ejemplo
       </p>
    """
    st.markdown(texto_html, unsafe_allow_html=True)

def about_page():
    pass
def main():
    st.title("Mi aplicacion con Session State")

    #Menu lateral
    menu = ["Home", "Settings", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    match choice:
        case "Home":
            home_page()
        case "Settings":
            settings_page()
        case "About":
            pass

if __name__ == "__main__":
    main()