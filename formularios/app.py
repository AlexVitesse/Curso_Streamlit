import streamlit as st

def inicio():
    st.header("Bienvenido a la aplicacion de tutorial de formularios")
    st.write("""
        Este tutorial te enseñara sobre los formularios  de streamlit y sus diversas caracteristicas
        - Creacion basica de formularios
        - Diferentes enfoques para crear formularios
        - Formularios con columnas (Calculadora de salario)
        - Funcionalidad de reinicio de formularios
    """)

def formulario():
    st.header("Formularios Basicos")
    st.write("Aprenderemos como crear un formulario basico en strewamlit")

    #Formulario basico
    with st.form(key="formulario_basico"):
        st.write("Formulario simple de registro")
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        boton_enviar = st.form_submit_button(label="Registrarse")
    if boton_enviar:
        st.success(f"Hola {nombre} Has creado una cuenta.")
        
def enfoques_formulario():
    st.header("Enfoques de formulario")
    #Enfoque 1
    with st.form(key="formulario_1"):
        st.write("Formulario 1 usando administrador de contexto")
        nombre_usuario = st.text_input("Nombre de usuario")
        enviar = st.form_submit_button(label="Registrarse")

    if enviar:
        st.success(f"bienvenido {nombre_usuario}")
    #Enfoque 2
    st.subheader("Formulario 2 usando st.form")
    formulario2 = st.form(key="formulario_2")
    formulario2.write("Formulario 2 usando st.form")
    puesto = formulario2.selectbox("Puesto de trabajo",["Cientifico de datos","Desarrollador","Doctor"])
    enviar2 = formulario2.form_submit_button(label="Enviar")

    if enviar2:
        st.info(f"Puesto seleccionado: {puesto}")

def calculadora_salario():
    st.header("Calculadora de salario")

    with st.form(key="calculadora_salario"):
        col1, col2, col3 = st.columns(3)

        with col1:
            tarifa_horaria = st.number_input("Tarifa por hora",min_value=0.0,format="%f")
        with col2:
            horas_semana = st.number_input("Horas por semana",min_value=0, max_value=168)
        with col3:
            calcular = st.form_submit_button(label="Calcular")
        if calcular:
            diario = tarifa_horaria * 8
            semanal = tarifa_horaria * horas_semana
            mensual = semanal * 4
            anual = semanal * 52
            st.subheader("Resultados")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Sueldo diario: ", f"${diario:.2f}")
                st.write("Sueldo semanal: ", f"${semanal:.2f}")

            with col2:
                st.feedback("Sueldo mensual: ", f"${mensual:.2f}")
                st.feedback("Sueldo anual: ", f"${anual:.2f}")

def reinicio_formulario():
    st.header("Reinicio de formulario")
    st.write("Aqui se muestra como reiniciar un formulario")

    with st.form(key="reinicio_formulario", clear_on_submit=True):
        entrada_usuario = st.text_input("Escribe algo")
        nombre = st.text_input("Escribe tu nombre")
        enviar = st.form_submit_button("Enviar")
    
    if enviar:
        st.success(f"Escribiste: {entrada_usuario}")
        st.info("Observa como el formulario se reinicia automaticamente")

def main():
    st.title("Tutorial de formularios")

    #Menu lateral
    menu = ["Inicio","Formulario", "Enfoques de formulario","Calculadora de salario","Reinicio de formulario"]
    choice  = st.sidebar.selectbox("Selecciona una opcion",menu)

    match choice:
        case "Inicio":
            inicio()
        case "Formulario":
            formulario()
        case "Enfoques de formulario":
            enfoques_formulario()
        case "Calculadora de salario":
            calculadora_salario()
        case "Reinicio de formulario":
            reinicio_formulario()
if __name__ == "__main__":
    main()
