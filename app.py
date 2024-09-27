import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))

# Desinging the Page
st.title('Image to Text Application')
user_input=st.text_input('Input Prompt')
upload_file=st.file_uploader('Upload the Image....',type=['jpg','jpeg','png'])

# Display the image on the page
from PIL import Image
img=''
if upload_file is not None:
    img=Image.open(upload_file)
    st.image(img,caption='Uploaded_Image',use_column_width=True)

#Function for Evaluating the Image and Annotating it.
def gemini_response(user_input,img):
    model=genai.GenerativeModel('gemini-1.5-flash')
    if user_input!='':
        response=model.generate_content([user_input,img])
    else:
        response=model.generate_content(img)
    return response.text

# 
submit=st.button('See Magic')

if submit:
    response=gemini_response(user_input=user_input,img=img)
    st.subheader('The Response is: ')
    st.write(response)