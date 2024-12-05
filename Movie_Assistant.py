import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

openai.api_key = user_api_key

#client = openai.OpenAI(api_key=user_api_key)
prompt = """ Act as an AI assistant in finding information about movies in English and Thai.
You will receive a name of a movie and you should provide information about the legal streaming platform
containing said movie available in Thailand region. 
Also suggest three other movies made by the same filmmaker below with short description about the movies.
Please respond with a JSON object containing the following fields: "movie_title", "streaming_platform", "director", "other_movie".
"""

st.title("Movie Platform :clapper:")
st.subheader("Let's watch a movie while also supporting the makers!!")
st.markdown("The AI can assist you in finding your favorite movie on online platforms!")

"""user_input = st.text_area("Enter movie name:", "Your input here")

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-2024-05-13",
        messages=messages_so_far
    )
    
    st.markdown('**AI response:**')
    generated_text = response.choices[0].message.content
    print(generated_text)"""
