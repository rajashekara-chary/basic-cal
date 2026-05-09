from helpers import *
import streamlit as st

st.title('calculator of two numbers')

# n1=int(input("enter your first number"))
# n2=int(input("enter your second number"))

n1=int(st.number_input("enter your number"))
n2=int(st.number_input("enter you second"))


operator=st.selectbox("operation",['addition','subtraction','multiplication',
                                   'division','power','floor division'])   # dropdown box 

# st.write("select operation on two numbers,")
# st.write("Enter 1 for Addition")
# st.write("Enter 2 for Subtraction")
# st.write("Enter 3 for Multiplication")
# st.write("Enter 4 for Division")
# st.write("Enter 5 for Power")
# st.write("Enter 6 for Floor Division")



#operator =int(st.number_input("enter operation"))
a=st.button('click')    # button for true
st.write(a)

if st.button("show result"):        # button for show result

    if operator=="multiplication":
        st.write(mul(n1,n2))

    elif operator=="addition":
        st.write(add(n1,n2))

    elif operator=="subtraction":
        st.write(sub(n1,n2))

    elif operator=="power":
        st.write(pow(n1,n2))

    elif operator=="division":
        st.write(div(n1,n2))

    elif operator=="floor division":
        st.write(floor(n1,n2))
    else:
        st.write("please enter valid option")