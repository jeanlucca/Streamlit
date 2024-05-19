import streamlit as st

st.title("Meu primeiro deploy")

slider = st.slider("Selecione um ano ", min_value=1995, max_value=2024)
st.write(f'O ano selecionado foi:{slider}')