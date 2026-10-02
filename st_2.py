import streamlit as st

st.set_page_config(page_title = "text input Demo")
st.title("text input Demo")

name = st.text_input("Enter your name:", placeholder="e.g.shanti")
st.write(f"Hello, {name}!")

secret = st.text_input("Enter your password:", type="password")
st.write(f"Your password has (len(secret)) characters.")

comments = st.text_area("Any additional comments", height = 150)
st.write(f"Your wrote (len(comments)) characters.")

if st.button("submit"):
    st.write("You clicked on submit!")

show_message = st.checkbox("Do you want an extra message?")
if show_message:
    st.write("This is the message. Have a good day!")