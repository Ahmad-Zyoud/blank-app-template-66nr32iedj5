import streamlit as st

num1 = st.slider("Number 1?", 0, 130, 25)
num2 = st.slider("Number 2?", 0, 130, 25)
st.write("Sum", sum(num1, num2))
