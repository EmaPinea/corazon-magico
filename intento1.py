import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Configuración de la página ---
st.set_page_config(page_title="Corazón 3D Interactivo", page_icon="❤️", layout="centered")

# CSS para fondo oscuro y títulos
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        color: #FF4B4B !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    p {
        color: #cccccc !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Prueba 1")
st.write("Gíralo, acércalo y obsérvalo desde cualquier ángulo.")

# --- Barra Lateral de Personalización ---
st.sidebar.header("🎨 Personaliza tu 3D")
# Opciones de paletas de colores rojizos/rosados
colorscale_opciones = {
    'Rojo Pasión': 'Reds_r', # _r significa reverso (más oscuro en el centro)
    'Rosa Suave': 'RdPu_r',
    'Fuego': 'Hot_r',
    'Púrpura': 'Purples_r'
}
eleccion_color = st.sidebar.selectbox("Elige la paleta de color:", list(colorscale_opciones.keys()))
opacidad = st.sidebar.slider("Opacidad (Transparencia):", 0.1, 1.0, 0.8)

# --- Lógica Matemática 3D (¡La parte compleja!) ---
# 1. Creamos un "cubo" de puntos invisibles (una rejilla 3D)
# Usamos menos puntos (60j) para que cargue rápido en el celular
X, Y, Z = np.mgrid[-3:3:60j, -3:3:60j, -3:3:60j]

# 2. La Ecuación Mágica del Corazón 3D
# Esta fórmula define qué puntos del cubo forman parte del corazón
# F(x,y,z) = (x^2 + (9/4)y^2 + z^2 - 1)^3 - x^2*z^3 - (9/80)y^2*z^3
values = (X**2 + (9/4)*Y**2 + Z**2 - 1)**3 - X**2*Z**3 - (9/80)*Y**2*Z**3

# --- Creación del Gráfico 3D ---
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0,     # Dibujamos la superficie exactamente donde la ecuación da 0
    isomax=0,
    surface_count=1, # Una sola "piel" para el corazón
    colorscale=colorscale_opciones[eleccion_color],
    opacity=opacidad,
    showscale=False, # Ocultar la barra de colores lateral
    caps=dict(x_show=False, y_show=False, z_show=False), # Quitar tapas planas si se corta
    lighting=dict(ambient=0.4, diffuse=0.5, roughness=0.9, specular=0.6, fresnel=0.2), # Efectos de luz
    hoverinfo="none" # No mostrar coordenadas al pasar el mouse
))

# --- Estética Final del Gráfico ---
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False), # Ocultar eje X
        yaxis=dict(visible=False), # Ocultar eje Y
        zaxis=dict(visible=False), # Ocultar eje Z
        bgcolor='rgba(0,0,0,0)',   # Fondo transparente del cubo 3D
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)) # Posición inicial de la cámara
    ),
    paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente de la figura
    margin=dict(l=0, r=0, t=0, b=0), # Márgenes mínimos
    height=600
)

# Mostrar el resultado
st.plotly_chart(fig, use_container_width=True)

st.caption("Prueba 1")
