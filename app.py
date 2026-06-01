import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)
#hii
model = ChatHuggingFace(llm=llm) 

st.header("this chatbot is developed by Akash Singh")
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#user_input=st.text_input("Enter your prompt")

if st.button("click here"):
    #result=model.invoke(user_input)
    st.write("hello")
