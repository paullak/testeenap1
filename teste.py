import streamlit as st


numero = st.select_slider("Grau de Satisfação", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])



st.text('Seu número é ' + str(numero))

