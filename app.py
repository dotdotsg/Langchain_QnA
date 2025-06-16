from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_openai_response(question, model):
    api_key = os.getenv("OPENAI_API_KEY")
    if model == "gpt-3.5-turbo":
        llm = ChatOpenAI(model_name=model, temperature=0.7, openai_api_key=api_key)
        return llm.predict(question)
    else:  # text-davinci-003 or other completion models
        llm = OpenAI(model_name=model, temperature=0.7, openai_api_key=api_key)
        return llm(question)
    # llm = OpenAI(get_openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo", temperature=0.7)
    # response = llm(question)
    # return response;

    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))
    # return llm.predict(question)

# Initialize the streamlit app

st.set_page_config(page_title="QnA with OpenAI", page_icon=":robot_face:")

st.title("QnA with OpenAI")
st.header("A Langchain Application for QnA with OpenAI")
model = st.selectbox("Select OpenAI model:", ["gpt-3.5-turbo", "text-davinci-003"])
question = st.text_input("Enter your question:", key="input")
response = get_openai_response(question, model) if question else None
submit = st.button("Submit")
if submit and question:
    st.write("Response from OpenAI:")
    st.write(response)


