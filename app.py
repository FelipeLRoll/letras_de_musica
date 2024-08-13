import requests
import streamlit as st

st.title("Letras de Músicas")

# Input fields with validation
banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")

# Function to fetch lyrics with error handling
@st.cache_data
def buscar_letra(banda, musica):
    if not banda or not musica:
        return None, "Nome da banda e música são obrigatórios."
    
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        letra = response.json().get("lyrics", "")
        if not letra:
            return None, "Letra não encontrada."
        return letra, None
    except requests.exceptions.RequestException as e:
        return None, f"Erro ao buscar a letra: {e}"

# Search button
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra, error = buscar_letra(banda, musica)
    if error:
        st.error(error)
        st.snow()
    else:
        st.balloons()
        st.success("Encontramos a letra :D")
        st.text(f"""Banda:  {banda} \nMúsica: {musica}""".upper())
        st.text(letra)


