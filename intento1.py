import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Nombre Corazón", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: white; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Para ti con mucho Cariño")

# Barra lateral para el nombre y color
nombre_input = st.sidebar.text_input("Ingresa el Nombre:", "Emanuel")
color_pincel = st.sidebar.color_picker("Color del Brillo:", "#FF4B4B")
densidad = st.sidebar.slider("Cantidad de nombres:", 20, 100, 50)

# --- Lógica Matemática ---
# Generamos puntos siguiendo la forma del corazón
t = np.linspace(0, 2 * np.pi, densidad)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Creamos la figura con Plotly para que sea interactiva
fig = go.Figure()

# Añadimos el nombre en cada coordenada (x, y)
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="text",
    text=[nombre_input] * len(t),
    textfont=dict(
        family="Dancing Script, cursive",
        size=18,
        color=color_pincel
    ),
    hoverinfo="none"
))

# Estética del gráfico (quitar ejes y fondo)
fig.update_layout(
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=650,
    margin=dict(l=0, r=0, t=0, b=0)
)

# Mostrar en Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown(f"<p style='text-align: center; color: gray;'>Creado por Emanuel Jacome</p>", unsafe_allow_html=True)
