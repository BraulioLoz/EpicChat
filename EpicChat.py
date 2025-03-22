# comando para correrlo: streamlit run EpicChat.py

import streamlit as st
import openai
import base64

################################
# Convertir imagen a base64
################################
def image_to_base64(path: str) -> str:
    """Lee un archivo de imagen y devuelve su contenido en base64 como string."""
    with open(path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode("utf-8")

################################
# Configuración de la página
################################
st.set_page_config(
    page_title="Epic Chat", 
    page_icon="🦖", 
    layout="centered", 
    initial_sidebar_state="auto"
)

# 1. CSS para agrandar la barra de st.chat_input (altura y ancho)
st.markdown("""
<style>
/* Aumentar altura y fuente del textarea dentro de st.chat_input */
div[data-testid="stChatInput"] textarea {
    min-height: 80px;    /* Ajusta para más/menos altura */
    font-size: 1.1rem;   /* Ajusta para texto más grande */
}

/* Controlar el ancho máximo y centrar */
div[data-testid="stChatInput"] {
    max-width: 800px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

################################
# Barra lateral
################################
with st.sidebar:
    # Logo grande
    st.image("images/epiclab.png", use_container_width=True)
    st.markdown("---")
    st.markdown("#### ¡Síguenos en redes!")

    # Convertimos cada ícono a base64
    youtube_b64  = image_to_base64("images/youtube.png")
    insta_b64    = image_to_base64("images/insta.png")
    linkedin_b64 = image_to_base64("images/linkedin.png")

    # Creamos un bloque HTML con <a> + <img> en base64
    # para que no haya problema de ícono roto
    social_html = f"""
    <p style="display: flex; justify-content: space-evenly; align-items: center; gap: 10px;">
      <a href="https://www.youtube.com/channel/UC_F-fDfWTIxtgnL9uyK-FNw" target="_blank">
        <img src="data:image/png;base64,{youtube_b64}" alt="YouTube" width="32" height="32" />
      </a>
      <a href="https://www.instagram.com/epiclabitam/?hl=en" target="_blank">
        <img src="data:image/png;base64,{insta_b64}" alt="Instagram" width="32" height="32" />
      </a>
      <a href="https://www.linkedin.com/company/epic-lab-itam/" target="_blank">
        <img src="data:image/png;base64,{linkedin_b64}" alt="LinkedIn" width="32" height="32" />
      </a>
    </p>
    """
    st.markdown(social_html, unsafe_allow_html=True)

################################
# Título principal
################################
st.title("Epic Chat")

################################
# Clave de OpenAI
################################
openai.api_key = st.secrets["OPENAI_API_KEY"]

################################
# Contexto de Mr. Epic
################################
SYSTEM_PROMPT = '''
Eres "Mr. Epic", el asistente oficial del EPIC Lab del ITAM.
Tu rol es:
1) Resolver dudas sobre el EPIC Lab y sus programas o proyectos.
2) Ayudar a los visitantes a empezar a desarrollar una idea o proyecto,
   recomendando mentores, profesores o recursos del EPIC Lab.
3) Ser amigable, pero profesional y claro en tus respuestas.

Información sobre el EPIC Lab:
EPIC Lab es el Centro ITAM de Creatividad, Innovación y Emprendimiento.
EPIC Lab es un espacio que fomenta la construcción de habilidades y
conocimientos de la población estudiantil de los diversos programas
académicos y universidades para incentivar su vocación emprendedora
e impulsar la generación de ideas de negocio con base tecnológica.
El EPIC Lab ofrece eventos, talleres y conferencias enfocados en
fortalecer las habilidades y los conocimientos de la comunidad
estudiantil en temas de innovación, tecnología y emprendimiento.

- Retos principales:
    1) Fortalecer la comunidad y el 'match' de mentores-equipos
    2) Aumentar la participación de mujeres (actualmente ~30%)
    3) Ampliar el alcance de su contenido

- No inventes datos si no estás seguro; contesta con lo que sepas o di que no
  tienes la información.
'''

################################
# Definir el modelo
################################
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

################################
# Historial de mensajes
################################
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial en pantalla
# Aquí forzamos el avatar "🦖" para assistant
for message in st.session_state.messages:
    avatar_icon = "🦖" if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.write(message["content"])

################################
# Chat input
################################
prompt = st.chat_input("¿Qué deseas Mad Fellow :D?")
if prompt:
    # (A) Guardar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # (B) Mostrarlo en pantalla
    with st.chat_message("user"):
        st.write(prompt)

    # (C) Preparar mensajes para OpenAI (incluir system)
    messages_for_openai = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    messages_for_openai.extend(st.session_state.messages)

    # (D) Llamar a OpenAI con streaming
    with st.chat_message("assistant", avatar="🦖"):
        with st.spinner("Mr. Epic está pensando..."):
            response_chunks = []
            placeholder = st.empty()
            current_text = ""

            completion = openai.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=messages_for_openai,
                temperature=0.8,
                top_p=1,
                stream=True
            )
            for chunk in completion:
                chunk_text = chunk.choices[0].delta.content or ""
                current_text += chunk_text
                placeholder.write(current_text)

    # (E) Guardar la respuesta completa en historial
    final_response = current_text
    st.session_state.messages.append({
        "role": "assistant",
        "content": final_response
    })
