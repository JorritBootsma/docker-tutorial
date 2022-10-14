import streamlit as st
import requests

BASE_URL = "https://docker-tutorial-python.azurewebsites.net/"

st.title("Fill in your details!")

if st.button("Give me the version number!"):
    url_suffix = "version_number"
    response = requests.post(BASE_URL + url_suffix)
    with st.spinner("Requesting version number"):
        st.write(response)
        st.write(response.json())
        st.write(response.json()["response"])
