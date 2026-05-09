from databases import d

import streamlit as st

def Bank_account(d):
    user_in=st.text_input("enter your name") 
    login=False
    found=False
    for key,val in d.items():
        if val['username']==user_in:
            
            st.write("user is available")
            found=True
            user=key
            
            for i in range(1,4):
                pin=st.text_input("enter your password")
                if val['password']==pin:
                     st.write("login sucess")
                     login=True
                     break
                else:
                    st.write(f"{3-i} attempts left")
            else:
                st.write('contact to respective branch account is blocked')
                val['access']="not available"
            break
   
    

    
            
    if found:
        pass
    else:
        st.write("user not found")
            
    
    if login:
         if d[user]['access']=="available":
             st.write("enter one option 1-withdraw,2-deposit,3-check_balance")
             operation=st.number_input("enter your option")
             if 1==operation:
                 # print(f"available balance{val['balance']}")
                 withdraw=st.number_input("enter your withdraw amount")
                 if withdraw>val['balance']:
                     st.write("in sufficient balance")
                 else:
                     bal=val['balance']
                     ab=bal-withdraw
                     val['balance']=ab
                     st.write(f"your balance={val['balance']}")
             elif 2==operation:
                 deposit=st.number_input("enter your deposit amount")
                 val['balance']+=deposit
                 st.write(f"your balance= {val['balance']}")
             elif 3==operation:
                 st.write(f"your balance= {val['balance']}")
            
         else:
             st.write("account is blocked contact respective branch")
                

