import json
import streamlit as st


# read data
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data







#save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)





    


# total income

def total_income(data):
    total_salary=0
    for i in data:
        if i['type']=="income":
            total_salary+=i['amount']
    # st.write(f"total income {total_salary}")
    return total_salary


# total expenses

def total_expense(data):
    total_expense=0.0
    for i in data:
        if i['type']=='expense':
            total_expense+=i['amount']

    # st.write(f" your total expenses {total_expense}")
    return total_expense
    

# remaining balance


def balance_income(data):
     balance= total_income(data)-total_expense(data)
     return balance


           



    



    