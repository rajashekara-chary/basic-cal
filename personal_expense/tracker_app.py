from transactions import *
import streamlit as st








data=load_data()

choose=st.selectbox('choice',['trasaction','new transactions','total income','total expenses','remaining balance','expense summary'])

if choose=="transaction":
    transactions(data)                         # to view transactions

elif choose=="new transaction":

    new_transactions(data)                            # to add new transaction

elif choose=="total income":

    salary=total_income(data)                  #print(salary)


elif choose=="total expense":

    expense=total_expense(data)

elif choose=="remaining balance":
    def balance_income(data):
        balance= salary-expense
        print(f"remaining balance {balance}")

    balance_income(data)
elif choose=="expense summary":
    summary(data)



