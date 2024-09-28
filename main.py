import streamlit as st

st.text("Teste")
salario = st.number_input("Salario: ", min_value=1, value=1)
resul = 1000000/int(salario)
resul2 = resul/12
st.button("Calcular")
st.text(f"Vais demorar {round(resul2)+1} anos para chegares a 1000000€")