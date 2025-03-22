# EpicChat

**EpicChat** es un chatbot construido con [Streamlit](https://streamlit.io/) y la API de [OpenAI](https://openai.com/) que sirve como asistente para el EPIC Lab del ITAM. Permite a los usuarios resolver dudas sobre programas, iniciativas y eventos, así como recibir orientación para desarrollar ideas o proyectos emprendedores.

## Tabla de Contenidos

1. [Características](#características)  
2. [Requisitos](#requisitos)  
3. [Instalación y Ejecución Local](#instalación-y-ejecución-local)  
4. [Configuración de la API Key de OpenAI](#configuración-de-la-api-key-de-openai)  
5. [Estructura del Proyecto](#estructura-del-proyecto)  
6. [Despliegue en Streamlit Cloud](#despliegue-en-streamlit-cloud)  
7. [Uso](#uso)  
8. [Personalización](#personalización)  
9. [Créditos y Licencia](#créditos-y-licencia)

---

## Características

- 💬 Interfaz tipo chat con experiencia conversacional.
- 🚀 Respuestas en tiempo real usando streaming de la API de OpenAI.
- 🎓 Contexto personalizado para apoyar a estudiantes del EPIC Lab.
- 🎨 Interfaz visual personalizada con logos e íconos de redes.
- ☁️ Fácil despliegue en Streamlit Cloud.

---

## Requisitos

- Python 3.9 o superior.
- Clave API válida de [OpenAI](https://platform.openai.com/account/api-keys).
- Dependencias listadas en `requirements.txt`.

---

## Instalación y Ejecución Local

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/EpicChat.git
cd EpicChat

# 2. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
# Actívalo:
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Corre la aplicación
streamlit run EpicChat.py
