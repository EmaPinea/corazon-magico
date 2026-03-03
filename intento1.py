import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Configuración de la Página ---
st.set_page_config(page_title="Corazón de Palabras 3D", page_icon="💖", layout="wide")

# Estilo visual
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #FF0055; text-align: center; text-shadow: 0 0 20px #FF0055; }
    p { color: #cccccc; text-align: center; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("     💖     ")
st.write("Tu nombre forma la estructura en 3D, asi q porq no lo giras")

# --- Barra Lateral ---
st.sidebar.header("🎨 Personaliza")
nombre = st.sidebar.text_input("Nombre:", "Emanuelle")
color = st.sidebar.color_picker("Color:", "#FF0055")
densidad = st.sidebar.slider("Densidad:", 500, 3000, 1500, step=100)
tamano = st.sidebar.slider("Tamaño:", 8, 20, 12)

# --- Matemáticas 3D ---
u = np.linspace(0, np.pi, int(np.sqrt(densidad)))
v = np.linspace(0, 2 * np.pi, int(np.sqrt(densidad)))
u, v = np.meshgrid(u, v)
u = u.flatten()
v = v.flatten()

x = 16 * np.sin(u)**3 * np.cos(v)
y = 16 * np.sin(u)**3 * np.sin(v)
z = 13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)

# --- Gráfico ---
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='text',
    text=[nombre] * len(x),
    textfont=dict(size=tamano, color=color, family="Arial"),
    hoverinfo='none'
))

# Configuración limpia (Aquí estaba el error, ya corregido con 'visible=False')
axis_args = dict(showbackground=False, showgrid=False, showticklabels=False, visible=False, zeroline=False)

fig.update_layout(
    dragmode='orbit', 
    scene=dict(
        xaxis=axis_args,
        yaxis=axis_args,
        zaxis=axis_args,
        bgcolor='rgba(0,0,0,0)',
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.2))
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    height=700
)

st.plotly_chart(fig, use_container_width=True)

