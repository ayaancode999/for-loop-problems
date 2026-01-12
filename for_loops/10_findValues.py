# Given a string, count how many vowels (`a, e, i, o, u`) it contains.
userinput=(input("give a word"))
vowel="a","e","i","o","u"
numberOfvowels=0
if vowel in userinput:
    numberOfvowels=numberOfvowels+1
print(numberOfvowels)