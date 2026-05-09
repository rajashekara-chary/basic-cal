from databases import *

def control(ad):
    admin=input("enter your admin username = ") 
    login=False

    for key,val in ad.items():
        if val['admin_name']==admin:
            print("admin is available")
            pin=int((input("enter your password = ")))
            if val['pass']==pin:
                print("login sucess")
                login=True
                break
            
            
    
    if login:
        user=input("enter username of a user = ")
        for key,val in d.items():
            if val['username']==user:
                val['access']="available"
                user_change=input("enter your new name for change = ")
                if user_change is None:
                    pass
                else:
                    val['username']=user_change
                pin_change=input("enter your new pin for change = ")
                if pin_change is None:
                    pass
                else:
                    val['password']=pin_change
                    

