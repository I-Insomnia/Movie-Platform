import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """ Act as an AI assistant in finding information about movies in English and Thai.
You will receive a name of a movie and you should provide information about the legal streaming platform
containing said movie available in Thailand region. 
Also suggest three other movies made by the same filmmaker below with short description about the movies.
"""

st.title("Movie Platform")
st.subheader("Let's watch a movie while also support the makers!!")

user_input = st.text_area("Enter movie name:", "Your input here")
