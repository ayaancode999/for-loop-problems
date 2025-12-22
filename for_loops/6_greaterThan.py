# Given a list of numbers, count how many are greater than 10.
#make list
#make variables to store numbers smaller or bigger than 10
# make for loop
#print numbers bigger than 10
x=[1,34,56,7,8,9,34,54,21,0,3,2,99,101,2,3,65,2.2,1,99.9,34,5]
greaterThan=0
lessThan=0
for number in x:
    if number>10:
        greaterThan=greaterThan+1
    else:
        lessThan=lessThan+1
print("numbers greater than ten are ", greaterThan)
