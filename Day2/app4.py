import streamlit as st 

st.title("Simple Chatbot!")

qn = st.text_input("Ask youer question : ")

if st.button("Send"):
    st.write(f"You asked {qn}?")
    st.write("Chatbot is on the process to reply your answer...")