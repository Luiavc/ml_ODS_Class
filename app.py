import os
import streamlit as st

path = "models/ods_pipeline.joblib"

st.write("Existe:", os.path.exists(path))
if os.path.exists(path):
    st.write("Tamaño bytes:", os.path.getsize(path))
    with open(path, "rb") as f:
        first_bytes = f.read(80)
    st.write("Primeros bytes:", first_bytes)