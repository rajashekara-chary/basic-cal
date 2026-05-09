from databases import *
import streamlit as st

def control(ad):
    # admin=input("enter your admin username = ") 
    admin=st.text_input("enter your admin username = ")
    login=False

    for key,val in ad.items():
        if val['admin_name']==admin:
            #print("admin is available")
            st.write("admin is avaialble")
            #pin=int((input("enter your password = ")))
            pin=st.number_input("enter your password = ")
            if val['pass']==pin:
                #print("login sucess")
                st.write("login sucess")
                login=True
                break
            
            
    
    if login:
        #user=input("enter username of a user = ")
        user=st.text_input("enter username of a user = ")
        for key,val in d.items():
            if val['username']==user:
                val['access']="available"
                #user_change=input("enter your new name for change = ")
                user_change=st.text_inut("enter your new name for change = ")
                if user_change is None:
                    pass
                else:
                    val['username']=user_change
                #pin_change=input("enter your new pin for change = ")
                pin_change=st.text_input("enter your new pin for change = ")
                if pin_change is None:
                    pass
                else:
                    val['password']=pin_change
                    

