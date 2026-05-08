from helpers import *

n1=int(input("enter your first number"))
n2=int(input("enter your second number"))

print("select operation on two numbers,")
print("mul,div,sub,add,pow,floor")


operator =input("enter operation")

if operator=="mul":
    print(mul(n1,n2))

elif operator=="add":
    print(add(n1,n2))

elif operator=="sub":
    print(sub(n1,n2))

elif operator=="pow":
    print(pow(n1,n2))

elif operator=="div":
    print(div(n1,n2))

elif operator=="floor":
    print(floor(n1,n2))
else:
    print("please enter valid option")