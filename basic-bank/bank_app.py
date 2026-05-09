
from admin_login import *
from customer_login import *

import streamlit as st

print("1. customer login")
print("2. admin Login")

choice = input("Enter choice: ")

if choice == "1":
    Bank_account(d)

elif choice == "2":
    control(ad)

else:
    print("Invalid Choice")