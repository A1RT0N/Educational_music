import cohere
import streamlit as st
from pydub import AudioSegment

co = cohere.Client("3lmg86xuofLDUK9UFR5mbvLNGwlVRHNw2IMjHeQm")

st.title("Your mnemonic")

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
            st.write("*Tema*:", title)

        with col2:
            st.write("*Keywords*:", keywords)

        st.write("*Artista*:", artista)

        audio_file_path = 'seu_audio.mp3'

        # Carregue o arquivo de áudio e reproduza automaticamente
        audio = AudioSegment.from_file(audio_file_path)
        play(audio)
