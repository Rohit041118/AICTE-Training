import streamlit as st


st.markdown("""
<style>
            st.Button > button{
            background-color: cyan;
            color: magenta;
            border-radius: 50%;
            }
            
               
</style>   
""",unsafe_allow_html=True) 



st.title("Basic Form!")

fname = st.text_input("Enter your first name : ")
lname = st.text_input("Enter your last name : ")
age = st.number_input("Enter your age : ")
email = st.text_input("Enter your email : ")
city = st.selectbox("Select your city : ", ["Nashik", "Pune", "Mumbai", "Delhi"])
edu = st.radio("Select your education : ", ["Phd", "PG", "UG", "HSC", "SSC", "7wi Fail"])

if st.button("Submit"):
    st.write(f"Hello {fname} {lname}!")
    st.write(f"Your age is {age} and you are from {city}!")
    st.write(f"Your email is {email} and your education is {edu}!")
