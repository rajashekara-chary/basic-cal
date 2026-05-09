from databases import *
import streamlit as st

def control(ad):
    admin=st.text_input("enter your admin username = ") 
    login=False

    for key,val in ad.items():
        if val['admin_name']==admin:
            st.write("admin is available")
            pin=st.number_input("enter your password = ")
            if val['pass']==pin:
                st.write("login sucess")
                login=True
                break
            
            
    
    if login:
        user=st.text_input("enter username of a user = ")
        for key,val in d.items():
            if val['username']==user:
                val['access']="available"
                st.write(" access updated")
        update=st.text_input("Do you want to change details? (yes/no): ")
        if update.lower()=='yes':
        
            st.write(" for username change enter (1), for pin change enter (2) ")
    
            change=st.number_input("choose your nummber")
            if change==1:
                user_change=st.text_input("enter your new name for change = ")
                val['username']=user_change
                st.write(f"your updated username {val['username']}")
            elif change==2:
                pin_change=st.text_input("enter your new pin for change = ")
                val['password']=pin_change
                st.write(f"your updated pin {val['password']}")
            else:
                st.write('invalid choice')
        else:
            st.write("no changes made")
            
                    

