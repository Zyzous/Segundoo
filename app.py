import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('todoeventos.png')

st.image(image, width=200)
