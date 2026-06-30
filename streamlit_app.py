import streamlit as st
import pandas as pd
from groq import Groq
class MyChatBot:
    def __init__(self,name,max_tokens,model):
        self.name= name
        st.title(name)
        st.header(name)
        self.client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
        )
        self.messages = []
        self.max_tokens=max_tokens
        self.model = model
    def generate_text(question):
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model=,
        max_tokens=self.max_tokens,
    )
    return chat_completion.choices[0].message.content

def generate_text(question,max_tokens):
    
chat_input = st.text_area("Ask Anything")
chat_submit_btn = st.button("Submit")
if chat_submit_btn:
    st.write(generate_text(chat_input,150))
    

def main():
    bot = MyChatBot("Groq Streamlit ChatBot",
                    150,
                    "llama-3.3-70b-versatile")
                    

#st.write(pd.DataFrame({"A": [1,2,3],"B":[4,5,6]}))
