import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='Q&A demo')
st.header('HI koyel!!')
status=load_dotenv(find_dotenv(),override=True)
st.write(status)
mykey=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=mykey)
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
#st.write(mykey)
def get_gemini_response(question):
   response=chat.send_message(question,stream=True)
   return response

# Initialize streamlit app

st.header('Gemini conversation application')
#initialize session state for chat history
if'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input=st.text_input("Input:",key="input")
submit=st.button("Ask The Question?")
if submit and input:
    response=get_gemini_response(input)
    #add the user quary and response to session state chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader('The chat histoty is')

for role,text in st.session_state['chat_history']:
    st.write(f"{role}  :  {text}")