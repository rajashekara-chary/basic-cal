
from admin_login import *
from customer_login import *

import streamlit as st

# st.write("1. customer login")
# st.write("2. admin Login")

st.title("one piece bank")

choice = st.selectbox('choice',{'customer login':1,'admin login':2})

if choice == "1":
    st.write(Bank_account(d))

elif choice == "2":
    st.write(control(ad))

# else:
#     st.write("Invalid Choice")