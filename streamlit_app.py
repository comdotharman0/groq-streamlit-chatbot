import streamlit as st
import pandas as pd
from groq import Groq
st.title("Groq Streamlit Chatbot")
st.header("Groq Streamlit Chatbot 🤖")
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)
def generate_text(question,max_tokens):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=max_tokens,
    )
chat_input = st.text_area("Ask Anything")
chat_submit_btn = st.button("Submit")

st.write(chat_completion.choices[0].message.content)

st.write(pd.DataFrame({"A": [1,2,3],"B":[4,5,6]}))
