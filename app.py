from helpers import *
import streamlit as st

st.title('calculator of two numbers')

# n1=int(input("enter your first number"))
# n2=int(input("enter your second number"))

n1=int(st.number_input("enter your number"))
n2=int(st.number_input("enter you second"))

st.write("select operation on two numbers,")
st.write("mul,div,sub,add,pow,floor")


operator =st.text_input("enter operation")

if operator=="mul":
    st.write(mul(n1,n2))

elif operator=="add":
    st.write(add(n1,n2))

elif operator=="sub":
    st.write(sub(n1,n2))

elif operator=="pow":
    st.write(pow(n1,n2))

elif operator=="div":
    st.write(div(n1,n2))

elif operator=="floor":
    st.write(floor(n1,n2))
else:
    st.write("please enter valid option")