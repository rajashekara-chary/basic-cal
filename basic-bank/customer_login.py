from databases import d

import streamlit as st

def Bank_account(d):
    # user_in=input("enter your name") 
    user_in=st.text_input("enter your name")
    login=False
    found=False
    for key,val in d.items():
        if val['username']==user_in:
            
                #print("user is available")
                st.write("user is available")
                found=True
                user=key
                
                for i in range(1,4):
                    #pin=(input("enter your password"))
                    pin=st.text_input("enter your pin")
                    if val['password']==pin:
                         #print("login sucess")
                         st.write("login sucess")
                         login=True
                         break
                    else:
                        #print(f"{3-i} attempts left")
                        st.write(f"{3-i} attempts left")
                else:
                    #print('contact to respective branch account is blocked')
                    st.write('contact to respective branch account is blocked')
                    val['access']="not available"
        else:
            #print("no access contact to respective branch")
            st.write("no access contact to respective branch")
            break

    
            
    if found:
        pass
    else:
        #print("user not found")
        st.write("user not found")
            
    
    if login:
         if d[user]['access']=="available":
             #print("enter one option 1-withdraw,2-deposit,3-check_balance")
             st.write("enter one option 1-withdraw,2-deposit,3-check_balance")
             #operation=eval(input("enter your option"))
             operation=st.number_input("enter your option")
             if 1==operation:
                 # print(f"available balance{val['balance']}")
                 # withdraw=eval(input("enter your withdraw amount"))
                 withdraw=st.number_input("enter your withdraw amount")

                 if withdraw>val['balance']:
                     #print("in sufficient balance")
                     st.write("insufficient balance")
                 else:
                     bal=val['balance']
                     ab=bal-withdraw
                     val['balance']=ab
                     #print(f"your balance={val['balance']}")
                     st.write(f"your balance={val['balance']}")
             elif 2==operation:
                 #deposit=eval(input("enter your deposit amount"))
                 deposit=st.number_input("enter your deposit amount")
                 val['balance']+=deposit
                 #print(f"your balance= {val['balance']}")
                 st.write(f"your balance= {val['balance']}")
             elif 3==operation:
                 #print(f"your balance= {val['balance']}")
                 st.write(f"your balance= {val['balance']}")
        