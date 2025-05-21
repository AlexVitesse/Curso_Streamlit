#Esta version guarda el contexto en un langchain
#Y consume informacion de internet
import streamlit as st
from openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

# Configuración de OPENAI
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=st.secrets.get("api_key"))

# Configuración de Google Search
search = GoogleSearchAPIWrapper(
    google_api_key=st.secrets.get("google_api_key"), 
    google_cse_id=st.secrets.get("google_cse_id")
)

# Herramienta de búsqueda
search_tool = Tool(
    name="Google Search",
    description="Busca en Google para obtener información actualizada.",
    func=search.run
)

# Configuración de LangChain
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

st.title("Chatbot con OpenAI")

# Crear variable de sesión de historia de chat
if "Messages" not in st.session_state:
    st.session_state.Messages = []

# Función para mostrar el historial
for message in st.session_state.Messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("¿En qué te puedo ayudar?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Agregar el mensaje del usuario a la historia de chat
    st.session_state.Messages.append({"role": "user", "content": prompt})
    st.session_state.memory.chat_memory.add_user_message(prompt)

    # Obtener respuesta de OpenAI o hacer búsqueda
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            # Verificar si el usuario solicita información de internet
            if "busca en internet" in prompt.lower():
                query = prompt.lower().replace("busca en internet", "").strip()
                with st.spinner("Buscando información en internet..."):
                    search_result = search_tool.run(query)

                # Procesar los resultados para que sean más legibles
                search_lines = search_result.split("\n")
                formatted_results = ""
                for line in search_lines:
                    if line.strip() and not line.startswith("..."):  # Filtrar ruido
                        formatted_results += f"- {line.strip()}\n"

                full_response = f"🔍 **Resultados de búsqueda:**\n{formatted_results}"

            else:
                # Obtener el historial de LangChain
                history = st.session_state.memory.load_memory_variables({})["history"]
                
                stream = client.chat.completions.create(
                    model="llama-3.2-90b-vision-preview",
                    messages=[
                        {"role": "system", 
                         "content": "Eres un asistente amable, servicial que solo da la informacion directa"},
                        *[{"role": "user", "content": history}]
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
            
            # Agregar la respuesta del asistente al historial
            st.session_state.Messages.append({"role": "assistant", "content": full_response})
            st.session_state.memory.chat_memory.add_ai_message(full_response)

            # Mostrar la respuesta inmediatamente
            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"Error al obtener respuesta: {e}")
