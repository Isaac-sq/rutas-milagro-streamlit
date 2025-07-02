import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Optimización de Rutas Milagro", layout="wide")
st.title("Optimización de Rutas de Transporte Urbano - Milagro")
st.write("""
Este proyecto aplica **álgebra lineal y programación lineal entera** para optimizar la ubicación de paradas de transporte en la ciudad de Milagro,
utilizando matrices de cobertura y escenarios simulados para maximizar la cobertura de zonas de demanda.
""")

# Datos simulados
paradas = ['Los Chirijos', 'Roberto Astudillo', 'Mariscal Sucre']
zona_demanda = ['San Antonio', 'Manantial', 'Bellavista', 'Las Piñas']
matriz_cobertura = np.array([
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1]
])

# Botón para mostrar resultados
def mostrar_graficos():
    st.subheader("Mapa de Cobertura Simulado")
    fig, ax = plt.subplots()
    for i, parada in enumerate(paradas):
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)
        circle = plt.Circle((x, y), 1.5, color='blue', alpha=0.2)
        ax.add_artist(circle)
        ax.text(x, y, parada, fontsize=9, ha='center')
    for j, zona in enumerate(zona_demanda):
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)
        ax.plot(x, y, 'ro')
        ax.text(x, y, zona, fontsize=9, ha='center', va='bottom')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_title("Mapa Simulado de Milagro")
    st.pyplot(fig)

    st.subheader("Matriz de Cobertura (Heatmap)")
    fig2, ax2 = plt.subplots()
    cax = ax2.matshow(matriz_cobertura, cmap='Blues')
    fig2.colorbar(cax)
    ax2.set_xticks(range(len(zona_demanda)))
    ax2.set_yticks(range(len(paradas)))
    ax2.set_xticklabels(zona_demanda)
    ax2.set_yticklabels(paradas)
    ax2.set_title("Matriz de Cobertura entre Paradas y Zonas de Demanda")
    st.pyplot(fig2)

    st.subheader("Gráfico de Cobertura por Escenario")
    escenarios = ['1 parada', '2 paradas', '3 paradas']
    zonas_cubiertas = [2, 3, 4]
    fig3, ax3 = plt.subplots()
    ax3.bar(escenarios, zonas_cubiertas, color='skyblue')
    ax3.set_xlabel("Escenario")
    ax3.set_ylabel("Zonas Cubiertas")
    ax3.set_title("Comparativa de Zonas Cubiertas según Escenario")
    st.pyplot(fig3)

if st.button("Mostrar Rutas y Gráficas"):
    mostrar_graficos()

st.info("Pulsa el botón para visualizar mapas, matrices de cobertura y comparativas de cobertura de zonas para la ciudad de Milagro.")