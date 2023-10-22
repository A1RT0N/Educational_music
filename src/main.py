import cohere
import streamlit as st

co = cohere.Client("3lmg86xuofLDUK9UFR5mbvLNGwlVRHNw2IMjHeQm")

st.title("Your mnemonic")

title = st.text_input("Enter an industry:", "")
#keywords = st.text_input("Enter an industry:", "")


creativity_options = ["Eminem", "Soon..."]
selected_creativity = st.selectbox("Select:", creativity_options)

if selected_creativity == "Eminem":
    artista = "Eminem"
elif selected_creativity == "Soon...":
    artista = Eminem
else:
    artista = Eminem

if st.button("Generate Idea"):
    st.subheader("Generated Mnmonic:")

    st.write("Tema: ", title)
    st.write("Artista: ", artista)
