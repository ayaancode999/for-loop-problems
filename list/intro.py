# creating a list using built in function list()
b=list(("hi",4,9.2))
print(b)
#making a repeatable list using multiply operator
c=[2]*5
print(c)
# accessing list with indexes
d=[2,4,6,9,0]
print(d[0])
#using append method
e=[3,4,5,6,7]
e.append("hi")
e.append("1")
e.append(2)
print(e)
#using extend method
f=[]
f.extend([2,3,4])
print(f)
#using insert method
g=[5,567,88]
g.insert(1,"hello")
print(g)
#using clear method
g.clear()
print(g)
#updating the list
a=[1,2,3,4,5]
a[2]=3.2
print(a)