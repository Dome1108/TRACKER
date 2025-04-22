
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_excel("./Track Investigación de Mercados.xlsx", sheet_name="BASE")

# Título
st.title("Dashboard de Proyectos de Investigación de Mercados")

# Sección: Visión General
st.header("Visión General")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Proyectos", len(df))
col2.metric("Proyectos Completos", df[df["ESTADO"] == "Completo"].shape[0])
col3.metric("Avance Promedio", f"{df['% COMPLETADO'].mean():.0%}")

# Gráfico de estado
st.subheader("Distribución de Proyectos por Estado")
estado_counts = df['ESTADO'].value_counts()
fig, ax = plt.subplots()
estado_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_ylabel("Cantidad de Proyectos")
ax.set_xlabel("Estado")
st.pyplot(fig)

# Filtro por año y tipo
st.sidebar.header("Filtros")
años = st.sidebar.multiselect("Selecciona año(s)", df["AÑO"].unique(), default=df["AÑO"].unique())
tipos = st.sidebar.multiselect("Selecciona tipo(s)", df["TIPO"].unique(), default=df["TIPO"].unique())
filtro_df = df[(df["AÑO"].isin(años)) & (df["TIPO"].isin(tipos))]

# Avance por tipo
st.subheader("Promedio de Avance por Tipo")
avance_tipo = filtro_df.groupby("TIPO")["% COMPLETADO"].mean().sort_values()
fig2, ax2 = plt.subplots()
avance_tipo.plot(kind='barh', ax=ax2, color='steelblue')
ax2.set_xlabel("% Completado Promedio")
st.pyplot(fig2)

# Proyectos por encargado
st.subheader("Cantidad de Proyectos por Encargado")
proyectos_encargado = filtro_df["ENCARGADO"].value_counts()
fig3, ax3 = plt.subplots()
proyectos_encargado.plot(kind='bar', ax=ax3, color='cornflowerblue')
ax3.set_ylabel("Cantidad de Proyectos")
st.pyplot(fig3)

# Tabla interactiva
st.subheader("Vista Detallada de Proyectos")
st.dataframe(filtro_df.reset_index(drop=True))
