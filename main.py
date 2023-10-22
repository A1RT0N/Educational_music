import cohere
from src.a import com_cohere
import streamlit as st
from pydub import AudioSegment
import numpy as np

co = cohere.Client("")

st.title("Your Mnemonic 📚")

title = st.text_input("Theme:", key="theme1")
keywords = st.text_input("Keywords:", key="theme2")

creativity_options = ["Select an artist", "Eminem", "Soon..."]
selected_creativity = st.selectbox("Select:", creativity_options)

if st.button("Generate Mnemonic"):
    # Verifique se os campos de entrada não estão vazios
    if not title or not keywords or selected_creativity == "Select an artist":
        st.error("Please fill in all fields before generating an idea.")
    else:
        if selected_creativity == "Eminem":
            artista = "Eminem"
        elif selected_creativity == "Soon...":
            artista = "Soon..."

        st.subheader("Generated Mnemonic:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("**Theme**:", title)

        with col2:
            st.write("**Keywords**:", keywords)
        with col3:
            st.write("**Artist**:", artista)

        letter = com_cohere(title, keywords)
        
        st.write("**Lyrics**:\n")
        
        st.write(letter)
        
        audio_file = open('output_audio.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')
