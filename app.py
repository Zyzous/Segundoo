import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('logoTodoEventos.png')

st.image(image, width=200)


try:
  os.mkdir("temp")
except:
  pass

st.subheader("Texto a audio")
st.write('Las funciones de texto a audio son fundamentales')
