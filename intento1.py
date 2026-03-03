import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Configuración de la Página ---
st.set_page_config(page_title="Corazón de Palabras 3D", page_icon="💖", layout="wide")

# CSS para estilo oscuro y neón
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
    }
    h1 {
        color: #FF0055 !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        text-shadow: 0 0 10px #FF0055, 0 0 20px #FF0055;
    }
    .stMarkdown p {
        color: #cccccc !important;
        text-align: center;
    }
    /* Ocultar menú hamburguesa y footer de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("💖 Nube de Palabras Volumétrica 💖")
st.write("Tu nombre forma la estructura en 3D. ¡Gíralo!")

# --- Barra Lateral de Personalización ---
st.sidebar.header("🎨 Diseña tu Corazón 3D")
nombre_usuario = st.sidebar.text_input("Escribe el Nombre:", "Emanuelle")
color_texto = st.sidebar.color_picker("Color del Neón:", "#FF0055")
densidad = st.sidebar.slider("Cantidad de Palabras (Densidad):", 500, 3000, 1500, step=100)
tamano_texto = st.sidebar.slider("Tamaño del Texto:", 8, 20, 12)

# --- Lógica Matemática 3D (Paramétrica) ---
# Usamos coordenadas esféricas modificadas para crear la superficie del corazón
# 'u' recorre la forma de "gajo" y 'v' da la vuelta completa
u = np.linspace(0, np.pi, int(np.sqrt(densidad)))
v = np.linspace(0, 2 * np.pi, int(np.sqrt(densidad)))
u, v = np.meshgrid(u, v)
u = u.flatten()
v = v.flatten()

# Fórmulas para las coordenadas X, Y, Z
x = 16 * np.sin(u)**3 * np.cos(v)
y = 16 * np.sin(u)**3 * np.sin(v)
z = 13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)

# --- Creación del Gráfico 3D con Texto ---
fig = go.Figure()

# Añadimos la "nube" de texto en 3D
fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='text',  # ¡Aquí está la magia! Modo texto, no puntos ni líneas
    text=[nombre_usuario] * len(x), # Repetimos el nombre para cada punto
    textfont=dict(
        family="'Dancing Script', cursive, Arial", # Fuente elegante
        size=tamano_texto,
        color=color_texto
    ),
    hoverinfo='none' # No mostrar nada al pasar el mouse para mantenerlo limpio
))

# --- Estética Final del Gráfico ---
axis_config = dict(
    showbackground=False, # Quitar paredes del cubo
    showgrid=False,       # Quitar rejilla
    showticklabels=False, # Quitar números
    showaxes=False,       # Quitar ejes
    zeroline=False,       # Quitar línea cero
    title=''              # Quitar títulos de ejes
)

fig.update_layout(
    scene=dict(
        xaxis=axis_config,
        yaxis=axis_config,
        zaxis=axis_config,
        bgcolor='rgba(0,0,0,0)', # Fondo transparente del escenario 3D
        camera=dict(
            eye=dict(x=1.8, y=1.8, z=1.2), # Posición inicial de la cámara
            center=dict(x=0, y=0, z=0)
        ),
        dragmode='orbit' # Modo de rotación orbital (más intuitivo en celular)
    ),
    paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente de la figura completa
    margin=dict(l=0, r=0, t=0, b=0), # Márgenes mínimos
    height=700 # Altura para que se vea grande en el celular
)

# Mostrar el resultado
st.plotly_chart(fig, use_container_width=True)

st.markdown(f"<p style='color: {color_texto} !important; font-style: italic;'>Visualización 3D interactiva creada con Python y Plotly.</p>", unsafe_allow_html=True)

