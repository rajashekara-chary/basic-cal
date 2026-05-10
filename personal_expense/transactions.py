import json


# read data
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data




# all transactions

def transactions(data):
    type_of_transaction=input("enter your type of trancation").lower()
    
    found=False
    if type_of_transaction=="all":
        print('-'*80)
        print(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
        print('-'*80)
        for i in data:
            print(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
        print('-'*80)


    else:
        print('-'*80)
        print(f"{'TYPE':<12}{'CATEGORY':<15}{'AMOUNT':<10}{'DATE':<15}{'DESCRIPTION'}")
        print('-'*80)
        for i in data:
            if i['type']==type_of_transaction:
                print(f"{i['type']:<12}{i['category']:<15}{i['amount']:<10}{i['date']:<15}{i['description']}")
                found=True
        print('-'*80)
        if not found:
            print("wrong spelling")


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
        new_transaction['type']=input("enter your type of transaction 'expesne or income' ").lower()
        new_transaction['category']=input("enter ")
        new_transaction['amount']=int(input("enter your amount"))
        new_transaction['date']=input("enter your date ,format dd-mm-yy")
        new_transaction['description']=input("enter your reason for category")
        break
    data.append(new_transaction)

    save_data(data)
    print("transaction added succesfully")
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
    print(f"total income {total_salary}")
    return total_salary


# total expenses

def total_expense(data):
    total_expense=0
    for i in data:
        if i['type']=='expense':
            total_expense+=i['amount']

    print(f" your total expenses {total_expense}")
    return total_expense
    

# remaining balance

# category wise expense summary

def summary(data):
    print('-'*30)
    print(f"{'category':<15}{'total spent':<15}")
    print('-'*30)
    for i in data:
        if i['type']=="expense":
            print(f"{i['category']:<15}{i['amount']:<15}")
    print('-'*30)
           



    



    