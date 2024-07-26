import streamlit as st

st.title("Welcome to My first Streamlit App")

name = st.text_input("Enter your name")

if name:
   st.write(f"Hello, {name}! Welcome to the app.")
