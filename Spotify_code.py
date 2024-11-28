#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importamos librerias, imagenes, y la base de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from skimage import io
spotify_df = pd.read_csv('./Datos/spotify_songs.csv')
sidebar = io.imread(r"./Imagenes/Bar.png")

#Portada
st.title("Análisis de datos de Spotify")
st.subheader(":green[En este proyecto, se pueden observar tres herramientas:"
            "**1.** Gráfico que muestra los subgéneros más escuchados por género músical"
            "**2.** Gráfico que muestra cuantas canciones fueron lanzadas según el mes"
            "**3.** Canción aleatoria con toda su información"
            "Esta información se generó gracias al siguiente DataFrame]")

#DataFrame
st.dataframe(spotify_df)
st.divider()

#Dashboard
st.sidebar.image(sidebar, width =220)
st.sidebar.markdown("#Configuración")
st.sidebar.divider()

#Definir columnas para gráficas
column_izq, column_mid, column_der = st.columns(3)

#Gráfico por Género
vars_genero = ["pop","rap","rock","latin","r&b","edm"]
default_gen = vars_genero.index("pop")
gen_select = st.sidebar.selectbox("Género para la gráfica", options = vars_genero)
st.sidebar.divider()

column_izq.subheader("Género")
fig1, ax1 = plt.subplots()

if gen_select == "pop":
    grafgen_df = pop_df
elif gen_select == "rap":
    grafgen_df = rap_df
elif gen_select == "rock":
    grafgen_df = rock_df
elif gen_select == "latin":
    grafgen_df = latin_df
elif gen_select == "r&b":
    grafgen_df = rb_df
elif gen_select == "edm":
    grafgen_df = edm_df
else:
    gen_select = grafgen_df
    
subgen_counts = grafgen_df["Subgenero"].value_counts()
ax1.set_title("Género y sus subgéneros más escuchados")
ax1.set_xlabel("Subgénero")
ax1.set_ylabel("Número de canciones")

#Gráfico por Años
vars_año = spotify_df["Año"].unique()
año_select = st.sidebar.selectbox("Año para la gráfica", options = vars_año)
añofilt_df = spotify_df[spotify_df["Año"] == año_select]

column_mid.subheader("Año")
fig2, ax2 = plt.subplots()

mes_counts = añofilt_df.groupby("Mes").size().reset_index(name = "Conteo")
ax2.bar(mes_counts["Mes"], mes_counts["Conteo"])
ax2.set_title("Canciones lanzadas por mes en el año: ")
ax2.set_xlabel("Més")
ax2.set_ylabel("Número de canciones")

#Información de Canción
def display_rndm_song():
    random_index = random.randint(0, len(df) - 1)
    random_song = spotify_df.iloc[random_index]
    st.write(f"**Nombre:** {random_song['Nombre']}")
    st.write(f"**Artista:** {random_song['Artista']}")
    st.write(f"**Popularidad:** {random_song['Popularidad']}")
    st.write(f"**Nombre del Album:** {random_song['Nombre del Album']}")
    st.write(f"**Lanzamiento:** {random_song['Lanzamiento'].date()}")
    st.write(f"**Playlist:** {random_song['Playlist']}")
    st.write(f"**Subgenero:** {random_song['Subgenero']}")
    st.write(f"**Duracion:** {random_song['Duracion']} seconds")

if st.sidebar.button ("Canción del día"):
    display_rndm_song(column_der)

