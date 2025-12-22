#define operators
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def divide(num1,num2):
    if num2==0:
        print("Division error")
    else:
        return num1/num2
def multiply(num1,num2):
    return num1*num2
#define calculator
def calculator():
    print("=== Simple Calculator ===\n")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Divide (/)")
    print("4. Multiply (*)")
    choice=float(input("Pick an operation (1-4):\n"))
    num1=float(input("Enter the first number:\n"))
    num2=float(input("Enter the second number:\n"))
    if choice==1:
        print("Answer =",add(num1,num2))
    elif choice==2:
        print("Answer =",subtract(num1,num2))
    elif choice==3: 
            print("Answer =",divide(num1,num2))
    elif choice==4:
        print ("Answer =",multiply(num1,num2))
    else:
        print("please try again")
calculator()

#make if statement and output