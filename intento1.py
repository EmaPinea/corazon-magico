import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Configuración de la Página ---
st.set_page_config(page_title="Corazón Elegante 3D", page_icon="💖", layout="wide")

# Estilo visual oscuro
st.markdown("""
    <style>
    .stApp { background-color: #020202; }
    h1 { color: #FF0055; text-align: center; font-family: 'Dancing Script', cursive; text-shadow: 0 0 15px #FF0055; }
    p { color: #aaaaaa; text-align: center; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("💖 Silueta 3D de Palabras 💖")
st.write("Una forma más elegante construida con tu nombre. ¡Gíralo!")

# --- Barra Lateral ---
st.sidebar.header("🎨 Personaliza")
nombre = st.sidebar.text_input("Nombre:", "Emanuelle")
color = st.sidebar.color_picker("Color Neón:", "#FF0055")
# Ajusté la densidad para esta nueva forma
densidad = st.sidebar.slider("Densidad de palabras:", 30, 100, 60)
tamano = st.sidebar.slider("Tamaño del texto:", 6, 18, 10)

# --- NUEVA MATEMÁTICA 3D (Forma más elegante) ---
# Usamos una parametrización diferente para una "cáscara" de corazón
u = np.linspace(0, 2 * np.pi, densidad)
v = np.linspace(0, np.pi, densidad)
u, v = np.meshgrid(u, v)
u = u.flatten()
v = v.flatten()

# Fórmulas nuevas para una silueta más definida
x = 16 * np.sin(u)**3 * np.sin(v)**2
y = (13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)) * np.sin(v)**2
# El factor 'z' aquí controla el grosor, lo hacemos más delgado
z = 6 * np.cos(v) * np.sin(u) 

# --- Gráfico ---
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='text',
    text=[nombre] * len(x),
    textfont=dict(size=tamano, color=color, family="Arial"),
    hoverinfo='none'
))

# Configuración limpia (SIN ERRORES)
axis_args = dict(showbackground=False, showgrid=False, showticklabels=False, visible=False, zeroline=False)

fig.update_layout(
    dragmode='orbit', # Rotación orbital suave
    scene=dict(
        xaxis=axis_args,
        yaxis=axis_args,
        zaxis=axis_args,
        bgcolor='rgba(0,0,0,0)',
        camera=dict(eye=dict(x=0, y=-2, z=0.5)) # Cámara frontal para ver la forma mejor
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    height=700
)

st.plotly_chart(fig, use_container_width=True)
