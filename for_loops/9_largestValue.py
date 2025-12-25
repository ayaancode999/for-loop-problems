# Given a list of numbers, find the largest value.
x=[3,5,6,89,32,45,6,1,0]
greatest=x[0]
for number in x:
    if number>greatest:
        greatest=number
print(greatest)
