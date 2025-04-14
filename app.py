import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Cargar el modelo
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

# Diccionarios de categorías
cut_dict = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
color_dict = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
clarity_dict = {"SI2": 1, "SI1": 2, "VS1": 3, "VS2": 4, "VVS2": 5, "VVS1": 6, "I1": 7, "IF": 8}

st.title("🪙 Predicción de precio de diamantes")
st.write("Introduce las características del diamante para predecir su precio.")

# Entrada de datos del usuario
carat = st.number_input("Carat", min_value=0.0, step=0.01, format="%.2f")
cut = st.selectbox("Cut", options=list(cut_dict.keys()))
color = st.selectbox("Color", options=list(color_dict.keys()))
clarity = st.selectbox("Clarity", options=list(clarity_dict.keys()))
depth = st.number_input("Depth (%)", min_value=0.0, step=0.1, format="%.1f")
table = st.number_input("Table (%)", min_value=0.0, step=0.1, format="%.1f")
vol = st.number_input("Volumen (mm³)", min_value=0.0, step=0.1, format="%.1f")

# Convertir categorías a números
cut_val = cut_dict[cut]
color_val = color_dict[color]
clarity_val = clarity_dict[clarity]

# Botón para hacer predicción
if st.button("Predecir precio"):
    entrada = np.array([[carat, cut_val, color_val, clarity_val, depth, table, vol]])
    prediccion = modelo.predict(entrada)[0]
    st.success(f"💎 El precio estimado del diamante es: ${prediccion:,.2f}")

