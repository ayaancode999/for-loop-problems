# Given a number `N`, find the sum of numbers from 1 to `N`.
# input: 5
# output: 15
#1+2+3+4+5
userinput=int(input("enter number"))
sum=0
for x in range(1,userinput+1):
    sum=sum+x
print(sum)