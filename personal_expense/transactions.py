import json
import streamlit as st


# read data
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data




# all transactions

def transactions(data):
    type_of_transaction=st.text_input("enter your type of trancation").lower()
    
    found=False
    if type_of_transaction=="all":
        st.write('-'*80)
        st.write(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
        st.write('-'*80)
        for i in data:
            st.write(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
        st.write('-'*80)


    else:
        st.write('-'*80)
        st.write(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
        st.write('-'*80)
        for i in data:
            if i['type']==type_of_transaction:
                st.write(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
                found=True
        st.write('-'*80)
        if not found:
            st.write("wrong spelling")


#save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)




# adding new transactions

def new_transactions(data):
    new_transaction={'type':'',
                 'category':'',
                 'amount':0,
                 'date':"",
                 'description':''}
    for key in new_transaction:
        new_transaction['type']=st.text_input("enter your type of transaction 'expesne or income' ").lower()
        new_transaction['category']=st.text_input("enter your category")
        new_transaction['amount']=st.number_input("enter your amount")
        new_transaction['date']=st.text_input("enter your date ,format dd-mm-yy")
        new_transaction['description']=st.text_input("enter your reason for category")
        break
    data.append(new_transaction)

    save_data(data)
    st.write("transaction added succesfully")
    # print('-'*80)
    # print(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
    # print('-'*80)
    # for i in t:
    #     print(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
    #     found=True


# total income

def total_income(data):
    total_salary=0
    for i in data:
        if i['type']=="income":
            total_salary+=i['amount']
    st.write(f"total income {total_salary}")
    return total_salary


# total expenses

def total_expense(data):
    total_expense=0
    for i in data:
        if i['type']=='expense':
            total_expense+=i['amount']

    st.write(f" your total expenses {total_expense}")
    return total_expense
    

# remaining balance

# category wise expense summary

def summary(data):
    st.write('-'*30)
    st.write(f"{'category':<15}{'total spent':<15}")
    st.write('-'*30)
    for i in data:
        if i['type']=="expense":
            st.write(f"{i['category']:<15}{i['amount']:<15}")
    st.write('-'*30)
           



    



    