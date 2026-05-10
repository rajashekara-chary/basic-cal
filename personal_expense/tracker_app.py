from transactions import *
import streamlit as st
import pandas as pd
import datetime



#st.title("Personal Expense Tracker")

st.sidebar.title('Navigation')

page=st.sidebar.radio('choose page',['home','view transaction','add transaction','summary'])

# st.sidebar.radio('home')
# st.sidebar.radio('add transactions')
# st.sidebar.radio('view transactions')
# st.sidebar.radio('summary')




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
            # st.write('-'*80)
            # st.write(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
            # st.write('-'*80)
            # for i in data:
            #     st.write(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
            # st.write('-'*80)
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


        


        # else:
        #     st.write('-'*80)
        #     st.write(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
        #     st.write('-'*80)
        #     for i in data:
        #         if i['type']==type_of_transaction:
        #             st.write(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
        #             found=True
        #     st.write('-'*80)
        #     if not found:
        #         st.write("wrong spelling")
        
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




















# choose=st.selectbox('choice',['trasaction','new transactions','total income','total expenses','remaining balance','expense summary'])

# if choose=="transaction":
#     transactions(data)                         # to view transactions

# elif choose=="new transaction":

#     new_transactions(data)                            # to add new transaction

# elif choose=="total income":

#     salary=total_income(data)                  #print(salary)


# elif choose=="total expense":

#     expense=total_expense(data)

# elif choose=="remaining balance":
#     def balance_income(data):
#         balance= salary-expense
#         print(f"remaining balance {balance}")

#     balance_income(data)
# elif choose=="expense summary":
#     summary(data)



