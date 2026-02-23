import streamlit as st


st.markdown("""
<style>
            .stButton > button{
                background-color: cyan; 
                color: magenta; 
                border-radius: 50%;
                }

</style>
""",unsafe_allow_html=True)






st.title("Welcome to basic streamlit app!")

age = st.slider("Select your age : ", 1, 100)

option = st.selectbox("Selectyour city : ",["Nashik", "Pune", "Mumbai", "Delhi"])
if st.button("Show details"):
    st.write(f"Your age is {age} and you are from {option}!")