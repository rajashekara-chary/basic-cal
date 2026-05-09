
from admin_login import *
from customer_login import *

import streamlit as st

# st.write("1. customer login")
# st.write("2. admin Login")

st.title("one piece bank")

choice = st.selectbox('choice',['customer login','admin login'])

if choice == "customer login":
    Bank_account(d)

elif choice == "admin login":
    control(ad)

# else:
#     st.write("Invalid Choice")