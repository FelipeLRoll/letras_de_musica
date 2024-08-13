import requests
import streamlit as st


st.title("Letras de musicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da musica: ", key="musica")

pesquisar = st.button("Pesquisar")

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

if pesquisar:
    
    letra = buscar_letra(banda, musica)
    if letra:
        st.balloons()
        st.success("Encontramos a letra :D")
        st.text( f"""Banda:  {banda} \nMusica: {musica}""".upper())
        st.text(letra)
    else:
        st.error("Infelizmente nao encontrei :/")   
        st.snow()



