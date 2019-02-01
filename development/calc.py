# this is introductory code
print("Calulator")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulous")

#funtions listed below
def add():
    print("add")
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    value= float(num1)+float(num2)
    print("sum is ",value)
    return value 

def sub():
    print("difference")
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    value = float(num1)-float(num2)
    print("difference is ",value)
    return value 

def mul():
    print("Multiply")
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    value = float(num1)*float(num2)
    print("product is ",value)
    return value 

def div():
    print("Division")
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    value = float(num1)/float(num2)
    print("division factor is ",value)
    return value 

def mod():
    print("Modulus")
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    value = float(num1)%float(num2)
    print("remainder is ",value)
    return value

def inv():
    print("Invalid reponse")



#driving code
num = {
        1: add,
        2: sub,
        3: mul,
        4: div,
        5: mod,
    }
#response checking
try:
    selection = int(input("make choice: "))
    if selection in num:
        num1, num2 = 0,0
    num.get(selection, inv)()
except:
    print('WHOOPS!')