import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

model = ChatHuggingFace(llm=llm) 

st.header("this chatbot is developed by Akash Singh")
user_input=st.text_input("Enter your prompt")

if st.button("click here"):
    result=model.invoke(user_input)
    st.write(result.content)
