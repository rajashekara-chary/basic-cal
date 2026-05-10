from transactions import *
import streamlit as st
import pandas as pd
import datetime



#st.title("Personal Expense Tracker")

st.sidebar.title('Navigation')

page=st.sidebar.radio('choose page',['home','view transaction','add transaction','summary'])





data=load_data()

if page=="home":
    st.title("💰 Personal Expense Tracker")
    st.write("This application helps users manage their income and expenses easily.")
    st.header("features")
    st.write("Add Income")
    st.write("Add Expenses")
    st.write("View Transactions")
    st.write("Calculate Balance")
    st.write("Category-wise Expense Summary")

elif page == 'view transaction':
    st.header(" 📑 View Transactions")
    def transactions(data):
        type_of_transaction=st.selectbox('choose history',['selected none','All','income','expense'])
        
        found=False
        if type_of_transaction=="All":
            
            df = pd.DataFrame(data)
            st.table(df)
        elif type_of_transaction=="income":
            filtered_data = []

            for i in data:

                if i['type'] == type_of_transaction:

                    filtered_data.append(i)
                    found = True
                    df = pd.DataFrame(filtered_data)

            st.table(df)
                    


        elif type_of_transaction=="expense":
            filtered_data = []

            for i in data:

                if i['type'] == type_of_transaction:

                    filtered_data.append(i)
                    found = True

                    df = pd.DataFrame(filtered_data)

            st.table(df)


        


        
    transactions(data)

    


elif page == 'add transaction':
    st.header("➕ Add Transaction")
    def new_transactions(data):
        
        new_transaction=st.selectbox("choose transaction",['selected none','income','expense'])
        if new_transaction=="income":
            new_transaction={}
            new_transaction['type']='income'
            new_transaction['category']=st.selectbox("choose your category",['salary','bonus','business','freelancing','other'])
            new_transaction['amount']=st.number_input("enter your amount")
            new_transaction['date']=st.text_input("enter your date, dd-mm-yyyy")
            new_transaction['description']=st.text_input("enter your reason for category")
            if st.button("Add Transaction"):
                data.append(new_transaction)
                st.write("transaction added succesfully")
            
            
        elif new_transaction=="expense":
            new_transaction={}
            new_transaction['type']='expense'
            new_transaction['category']=st.selectbox("choose your category",['shopping','bills','education','food','traveling','income tax','other'])
            new_transaction['amount']=st.number_input("enter your amount")
            new_transaction['date']=st.text_input("enter your date ,dd-mm-yyyy")
            new_transaction['description']=st.text_input("enter your reason for category")
            if st.button("Add Transaction"):
                data.append(new_transaction)
                st.write(" ✅ transaction added succesfully")

        save_data(data)
        
    new_transactions(data)


elif page == 'summary':
    st.header("📊 Budget Overview")
    
    #st.header(total_income(data))
    st.header(f"Total Income: ₹ {total_income(data)}")
    
    
    st.header(f"Total Expense : ₹ {total_expense(data)}")


    st.header(f"Balance Income : {balance_income(data)}")
    
    st.write('-'*80)
    
    def summary():
        st.header("expense summary")
        expense_data = []

        for i in data:

            if i['type'] == "expense":

                expense_data.append({
                    'category': i['category'],
                    'total spent': i['amount']
                })

        df = pd.DataFrame(expense_data)
        


        st.table(df)
    summary()






















