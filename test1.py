import streamlit as st
from TWEAKS import TWEAKS
from llama import main

# Streamlit app design
st.title("🦜🔗Llama Flow Runner")

st.header("Enter the required API keys and tokens")
image_generation_MLAIapi_key = st.text_input("Image Generation MLAI API Key", type="password")
instagram_graph_api_token = st.text_input("Instagram Graph API Token", type="password")
instagram_user_id = st.text_input("Instagram User ID")
groq_api_key = st.text_input("Groq API Key", type="password")


st.header("Enter your message")
user_message = st.text_input("Message")


if st.button("Run Flow"):

    if image_generation_MLAIapi_key and instagram_graph_api_token and instagram_user_id and groq_api_key and user_message:
        # Update TWEAKS dictionary with user inputs
        TWEAKS['CustomComponent-zgHJ0']['image_generation_MLAIapi_key'] = image_generation_MLAIapi_key
        TWEAKS['CustomComponent-zgHJ0']['instagram_graph_api_token'] = instagram_graph_api_token
        TWEAKS['CustomComponent-zgHJ0']['instagram_user_id'] = instagram_user_id
        TWEAKS['GroqModel-gOn12']['groq_api_key'] = groq_api_key

        
        # Run the Llama flow
        main(user_message, TWEAKS)

        st.success("Flow executed successfully!")
    else:
        st.error("Please fill in all the fields")

print('Success!')
