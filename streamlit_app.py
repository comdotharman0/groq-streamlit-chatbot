import streamlit as st
import pandas as pd
from groq import Groq,RateLimitError,APIConnectionError, AIStatusError
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
        model=self.model,
        max_tokens=self.max_tokens,
    )
    return chat_completion.choices[0].message.content

chat_input = st.text_area("Ask Anything")
chat_submit_btn = st.button("Submit")
if chat_submit_btn:
    st.write(generate_text(chat_input,150))
    

def main():
    try:
        bot = MyChatBot("Groq Streamlit ChatBot",
                    150,
                    "llama-3.3-70b-versatile")
    except RateLimitError as rle:
        st.write("Got "+str(rle))
    except APIConnectionError as ace:
        st.write("Got "+str(ace))
    except AIStatusError as ase:
        st.write("Got "+str(ase))
    finally:
        st.write("That's All!")
if __name__=="__main__":
    main()
    

#st.write(pd.DataFrame({"A": [1,2,3],"B":[4,5,6]}))
