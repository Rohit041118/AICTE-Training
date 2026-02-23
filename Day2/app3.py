import streamlit as st  

st.title("Basic Calculator!")
num1 =  st.number_input("Enter first number : ", format="%f")
num2 =  st.number_input("Enter second number : ", format="%f")

operation = st.selectbox("Select operation : ", ["Add", "Sub", "Mult", "Div"])

if st.button("Calculate"):
    if operation == "Add":
        st.write(num1 + num2)
    elif operation == "Sub":
        st.write(num1 - num2)
    elif operation == "Mult":
        st.write(num1 * num2)
    elif operation == "Div":
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.write("Error: Division by zero is not allowed.")

    else :
        st.write("Invalid operation selected!")