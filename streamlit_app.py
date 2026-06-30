import streamlit as st
from groq import Groq
st.title("Groq Streamlit Chatbot")
St.header("Groq Streamlit Chatbot 🤖")
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

st.write(chat_completion.choices[0].message.content)

