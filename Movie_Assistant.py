import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

openai.api_key = user_api_key

prompt = """Act as an AI writing tutor in English. You will receive a 
            piece of writing and you should give suggestions on how to improve it.
            List the suggestions in a JSON array, one suggestion per line.
            Each suggestion should have 4 fields:
            - "before" - the text before the suggestion
            - "after" - the text after the suggestion
            - "category" - the category of the suggestion one of "grammar", "style", "word choice", "other"
            - "comment" - a comment about the suggestion
            Don't say anything at first. Wait for the user to say something.
        """    

st.title('Writing tutor')
st.markdown('Input the writing that you want to improve. \n\
            The AI will give you suggestions on how to improve it.')

user_input = st.text_area("Enter some text to correct:", "Your text here")

# Submit button after text input
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
            # Extract the AI's response
            suggestion_dictionary = response.choices[0].message.content

            # Parse JSON and convert to DataFrame
            try:
                sd = json.loads(suggestion_dictionary)
                suggestion_df = pd.DataFrame.from_dict(sd)
                st.markdown('**AI response:**')
                st.table(suggestion_df)
            except json.JSONDecodeError:
                st.error("The response is not in valid JSON format. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
