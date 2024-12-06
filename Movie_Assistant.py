import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

openai.api_key = user_api_key

prompt = """ Act as an movie and media master in finding information about movies in English.
You will receive a name of a movie and you should provide information about all legal streaming platform available in Thailand region 
with format that concat with ",".
Also suggest three other movies made by the same director below with short description about the movies. 
Answer only in English.
Please respond with a JSON object containing the following fields: "movie_title", "streaming_platform", "director", "other_movie".
Please suggests information with clearlify references and have provable references.
"""

st.title("Movie Platform :clapper:")
st.subheader("Let's watch a movie while also supporting the makers!!")
st.markdown("The Movie Platform AI will help you in finding your favorite movie on legal online platforms!")

user_input = st.text_area("Enter movie name in English:", "Your input here")

if st.button('Submit'):
    if not user_api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        messages_so_far = [
            {"role": "system", "content": prompt},
            {'role': 'user', 'content': user_input},
        ]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages_so_far
            )
            
            suggestion_dictionary = response.choices[0].message.content
            
            try:
                sd = json.loads(suggestion_dictionary)
                suggestion_df = pd.DataFrame.from_dict(sd)
                st.write(f"**Movie Title:** {sd['movie_title']}")
                st.write(f"**Streaming Platform:** {sd['streaming_platform']}")
                st.write(f"**Director:** {sd['director']}")
                st.write(f"**Suggestions movie from the same director:**")
                st.write(sd['other_movie'])
                
            except json.JSONDecodeError:
                st.error("The response is not in valid JSON format. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
