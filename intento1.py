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
densidad = st.sidebar.slider("Cantidad de Palabras:", 500, 3000, 1500, step=100)
tamano_texto = st.sidebar.slider("Tamaño del Texto:", 8, 20, 12)

# --- Lógica Matemática 3D ---
u = np.linspace(0, np.pi, int(np.sqrt(densidad)))
v = np.linspace(0, 2 * np.pi, int(np.sqrt(densidad)))
u, v = np.meshgrid(u, v)
u = u.flatten()
v = v.flatten()

x = 16 * np.sin(u)**3 * np.cos(v)
y = 16 * np.sin(u)**3 * np.sin(v)
z = 13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)

# --- Creación del Gráfico 3D ---
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='text',
    text=[nombre_usuario] * len(x),
    textfont=dict(
        family="Arial",
        size=tamano_texto,
        color=color_texto
    ),
    hoverinfo='none'
))

# --- Estética Final (AQUÍ ESTABA EL ERROR, YA ESTÁ ARREGLADO) ---
axis_config = dict(showbackground=False, showgrid=False, showticklabels=False, showaxes=False, zeroline=False, title='')

fig.update_layout(
    dragmode='orbit', # <--- Ahora está en el lugar correcto
    scene=dict(
        xaxis=axis_config,
        yaxis=axis_config,
        zaxis=axis_config,
        bgcolor='rgba(0,0,0,0)',
        camera=dict(
            eye=dict(x=1.8, y=1.8, z=1.2),
            center=dict(x=0, y=0, z=0)
        )
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    height=700
)

st.plotly_chart(fig, use_container_width=True)
st.markdown(f"<p style='color: {color_texto};'>Visualización 3D creada con Python.</p>", unsafe_allow_html=True)
