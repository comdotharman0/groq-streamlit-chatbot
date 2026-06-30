import streamlit as st
import pandas as pd
"""from groq import Groq
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
"""
st.write(pd.DataFrame({"A": [1,2,3],"B":[4,5,6}))
