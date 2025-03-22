# EpicChat

**EpicChat** es un chatbot construido con [Streamlit](https://streamlit.io/) y la API de [OpenAI](https://openai.com/) que sirve como asistente para el EPIC Lab del ITAM. Su objetivo es resolver dudas sobre programas, iniciativas y eventos, además de orientar a estudiantes en el desarrollo de ideas y proyectos emprendedores.

---

## 📌 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación y Ejecución Local](#instalación-y-ejecución-local)
- [Configuración de la API Key de OpenAI](#configuración-de-la-api-key-de-openai)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Personalización](#personalización)
- [Créditos](#créditos)

---

## Características

- 💬 Interfaz tipo chat con respuestas en tiempo real.
- 🦖 Asistente virtual personalizado "Mr. Epic".
- 📖 Contexto programable para guiar conversaciones.
- 🎨 Interfaz personalizable con logos e íconos.
- ☁️ Despliegue sencillo en Streamlit Cloud.

---

## Requisitos

- Python 3.9 o superior.
- API Key de OpenAI.
- Dependencias en `requirements.txt`:

```text
streamlit
openai
```

---

## Instalación y Ejecución Local

```bash
# Clona el repositorio
git clone https://github.com/TU_USUARIO/EpicChat.git
cd EpicChat

# (Opcional) Crea y activa un entorno virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la app
streamlit run EpicChat.py
```

---

## Configuración de la API Key de OpenAI

### Método recomendado: Archivo `secrets.toml`

1. Crea una carpeta `.streamlit`.
2. Dentro crea `secrets.toml` con:

```toml
OPENAI_API_KEY = "tu-api-key"
```

En tu código:

```python
import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
```

---

## Estructura del Proyecto

```
EpicChat/
├── images/
│   ├── epiclab.png
│   ├── youtube.png
│   ├── insta.png
│   └── linkedin.png
├── .streamlit/
│   └── secrets.toml
├── requirements.txt
├── EpicChat.py
└── README.md
```

---

## Uso

- Abre la aplicación.
- Ingresa preguntas en la barra inferior.
- Recibe respuestas inmediatas y sugerencias útiles sobre el EPIC Lab.

---

## Personalización

- Cambia logos en la carpeta `images/`.
- Modifica `SYSTEM_PROMPT` para ajustar la personalidad de Mr. Epic.
- Añade estilos personalizados vía CSS con:

```python
st.markdown("<style>...</style>", unsafe_allow_html=True)
```

---

## Créditos

- Desarrollado por: Braulio Alejandro Lozano Cuevas
- Tecnologías: [Streamlit](https://streamlit.io/) y [OpenAI](https://openai.com/)


---

¡Disfruta usando EpicChat! 🚀🦖
