import streamlit as st
import joblib

modelo = joblib.load("models/ods_pipeline.joblib")

st.title("Clasificador de ODS")

texto = st.text_area("Ingrese un texto")

if st.button("Clasificar"):
    pred = modelo.predict([texto])[0]
    st.write(f"ODS predicho: {pred}")
    