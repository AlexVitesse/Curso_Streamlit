import streamlit as st
from openai  import OpenAI

#Configuracion de OPENAI
client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key= st.secrets.get("api_key"))

st.title("Chatbot con OpenAI")

#Crear variable de sesion de historia de chat
if "Messages" not in st.session_state:
    st.session_state.Messages = []

#Funcion para mostrar el historial
for message in st.session_state.Messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Chat input
if prompt := st.chat_input("¿En que te puedo ayudar?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #Agregar el mensaje del usuario a la historia de chat
    st.session_state.Messages.append({"role": "user", "content": prompt})

    #obtener respuesta de openai
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            stream = client.chat.completions.create(
                model="llama-3.2-90b-vision-preview",
                messages=[
                    {"role": "system", 
                     "content": "Eres un asistente grosero, que responde muy cortante y ofendiendo"},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.Messages]
                ],
                stream=True
            )
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.Messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error al obtener respuesta de OpenAI: {e}")