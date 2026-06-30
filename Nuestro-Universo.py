import streamlit as st
import numpy as np
import plotly.graph_objects as go
import streamlit
import plotly
import pandas

# 1. Configuración de la página
st.set_page_config(page_title="Simulador del Universo", layout="wide")
st.title("🌌 Simulador Interactivo del Universo")
st.markdown("Explora un universo generado proceduralmente. Ajusta los parámetros en la barra lateral izquierda.")

# 2. Barra lateral para controles
st.sidebar.header("⚙️ Parámetros del Universo")
num_galaxies = st.sidebar.slider("Número de Galaxias", min_value=1, max_value=10, value=5)
stars_per_galaxy = st.sidebar.slider("Estrellas por Galaxia", min_value=100, max_value=5000, value=1000)
expansion_rate = st.sidebar.slider("Tasa de Expansión", min_value=0.1, max_value=2.0, value=1.0)
seed = st.sidebar.slider("Semilla del Universo", min_value=1, max_value=100, value=42)

# 3. Generación de datos (Simulación del Universo)
np.random.seed(seed)
x, y, z, colors, sizes, names = [], [], [], [], [], []

galaxy_types = ["Espiral", "Elíptica", "Irregular"]

for i in range(num_galaxies):
    # Centro de cada galaxia
    cx, cy, cz = np.random.normal(0, 10 * expansion_rate, 3)
    # Cantidad y dispersión
    n_stars = int(stars_per_galaxy * np.random.uniform(0.5, 1.5))
    spread = np.random.uniform(1.0, 5.0)
    
    # Coordenadas locales
    sx = np.random.normal(cx, spread, n_stars)
    sy = np.random.normal(cy, spread, n_stars)
    sz = np.random.normal(cz, spread, n_stars)
    
    x.extend(sx)
    y.extend(sy)
    z.extend(sz)
    
    # Propiedades visuales de las estrellas
    g_type = np.random.choice(galaxy_types)
    color_scale = np.random.choice(['Blues', 'YlOrRd', 'Magma'])
    colors.extend(np.random.random(n_stars))
    sizes.extend(np.random.uniform(1, 4, n_stars))

# 4. Crear visualización con Plotly 3D
fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=sizes,
        color=colors,
        colorscale='Viridis', # Colores del espacio profundo
        opacity=0.8
    )
)])

# Ajustes de la cámara y diseño del espacio
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        bgcolor="rgba(0,0,0,1)",
        xaxis=dict(showbackground=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showticklabels=False, title='')
    )
)

# 5. Mostrar en la app
st.plotly_chart(fig, use_container_width=True)
