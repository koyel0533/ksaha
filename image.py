import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='Image demo')
st.header('HI koyel!!')
status=load_dotenv(find_dotenv(),override=True)
st.write(status)
mykey=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=mykey)
def get_gemini_response_image(input,image):
 model=genai.GenerativeModel('gemini-1.5-flash-latest')

 if input!='':
   response=model.generate_content([input,image])
 else:
   response=model.generate_content(image)
 return response.text

input=st.text_input("Input Prompt",key="input")
u=st.file_uploader("choose an Image..",type=['jpg','jpeg','png'])
image=""
if u is not None:
  image=Image.open(u)
  st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("tell me something about the image")

if submit:
  response=get_gemini_response_image(input,image)
  st.subheader("The response is")
  st.write(response)
