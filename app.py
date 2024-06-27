# Import Liabraries
import streamlit as st
# import openai
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load the API key from the .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
openai_base_url = os.getenv('OPENAI_URL')


llm = ChatOpenAI(openai_api_base=openai_base_url, temperature=0.5)

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")


# Setup a Session state message variable to hold all the old message
if 'messages' not in st.session_state:
    st.session_state.messages = []   

# Display all the messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])


# Get the prompt
prompt = st.chat_input('Pass your Prompt here')

# If the user hits enter them
if prompt:
    # Display the prompt
    st.chat_message('user').markdown(prompt)
    # Add the prompt to the message history
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    # send the prompt to the llm
    response = llm.predict(prompt)
    # Display the response
    st.chat_message('assistant').markdown(response)
    # Add the response to the message history
    st.session_state.messages.append({'role': 'assistant', 'content': response})

