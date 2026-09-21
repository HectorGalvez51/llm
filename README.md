# Asistente de Escritura Automática ✍️

Asistente de escritura impulsado por IA con dos interfaces:

1. **Consola con OpenAI (`main.py`)** — versión principal de este curso (Fases 1-4).
2. **Web con Streamlit + Google Gemini (`asistente_escritura/app.py`)** — versión alternativa ya existente en el repo.

## 🚀 Funcionalidades (ambas versiones)

1. **Mejorar redacción y ortografía**: corrige gramática y estilo.
2. **Sugerir continuación**: continúa un texto inicial con un párrafo coherente.
3. **Escribir un texto desde cero**: genera un texto completo a partir de un tema y un tono (Profesional, Casual, Creativo, Persuasivo).

## 🛠 Requisitos Previos

- Python 3.8 o superior.
- Una **API Key de OpenAI** (para `main.py`, obtenla en <https://platform.openai.com/api-keys>).
- (Opcional, solo versión web) Una **API Key de Google Gemini** desde [Google AI Studio](https://aistudio.google.com/).
- Git.

## 📦 Instalación

### 1. Fork y clonación (Fase 1)

En GitHub, haz **Fork** del repositorio oficial y luego clona **tu fork**:

```bash
git clone https://github.com/TU-USUARIO/llm.git
cd llm
```

### 2. Entorno virtual (Fase 1)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 3. Dependencias

Versión consola (OpenAI):

```bash
pip install -r requirements.txt
```

Versión web (Gemini + Streamlit):

```bash
pip install -r asistente_escritura/requirements.txt
```

## 🔑 Configuración de credenciales (Fase 2)

La versión de consola usa la variable de entorno `OPENAI_API_KEY`:

```bash
# Mac/Linux
export OPENAI_API_KEY='tu-clave-aqui'

# Windows (PowerShell)
$env:OPENAI_API_KEY='tu-clave-aqui'

# Windows (CMD)
set OPENAI_API_KEY=tu-clave-aqui
```

## ▶️ Uso

### A) Consola con OpenAI (Fases 2 y 3)

Prueba de conexión:

```bash
python main.py --test
# o desde el menú, opción 4
```

Menú interactivo:

```bash
python main.py
```

Opciones del menú:

- `1` Corrección de gramática y estilo.
- `2` Generación de texto completo a partir de un tema.
- `3` Sugerencia de continuación de oraciones.
- `4` Probar conexión con OpenAI.
- `0` Salir.

### B) Web con Streamlit + Gemini (versión existente)

```bash
streamlit run asistente_escritura/app.py
```

Abre `http://localhost:8501` e ingresa tu API Key de Gemini en la interfaz.

## 📁 Estructura del proyecto

```text
llm/
├── main.py                        # App de consola con OpenAI (Fases 2-3)
├── requirements.txt               # Dependencia: openai
├── asistente_escritura/
│   ├── app.py                     # App web Streamlit + Gemini
│   └── requirements.txt           # streamlit, google-generativeai
├── README.md
└── LICENSE
```

## 📚 Tecnologías Utilizadas

- [Python](https://www.python.org/)
- [OpenAI API](https://platform.openai.com/docs/) (versión consola)
- [Streamlit](https://streamlit.io/) (versión web)
- [Google Generative AI](https://ai.google.dev/) (versión web)
