import os
import requests
import streamlit as st

PROD_URL = "https://docker-tutorial-python.azurewebsites.net/"
DEV_URL = "127.0.0.1:8080"

BASE_URL = PROD_URL if os.environ["PROD"] else DEV_URL

st.title("Fill in your details!")

if st.button("Give me the version number!"):
    url_suffix = "version_number"
    response = requests.get(BASE_URL + url_suffix)
    with st.spinner("Requesting version number"):
        st.write(response)
        st.write(response.json())
        st.write(response.json()["response"])
