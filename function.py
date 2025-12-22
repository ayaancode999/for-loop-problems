def printer():
    userinput=input("enter your name")
    print("hello",userinput)


def add():
    userinput=int(input("enter a number"))
    userinput2=int(input("enter a another number"))
    answer=userinput+userinput2
    print(answer)


def multiply(num1,num2):
    return num1*num2
# print(multiply(3,5))

def divide(num1,num2):
    if num2==0:
        print("division by zero")
    else:
        return num1/num2
print(divide(2,1))
 