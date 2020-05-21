"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other """

"""
tech tech ==>length
tech thec ==>eqaul


"""
"""
tech=>ceth
thec=>ceth
"""

"""
Using sorting

a,b=input("Enter the string : ").split(" ")
a=sorted(a)
b=sorted(b)
if(len(a)==len(b)):
    if(a==b):
        print("Permutation")
else:
    print("No permutation")

"""

"""
teche tecch =>equal
tech
t=1 t=1
e=1 e=1
c=1 c=1
h=1 h=1


"""
"""
#count character
a,b=input("Enter the string : ").split(" ")
a=list(a)
b=list(b)
temp=a+b
temp=set(temp)
temp=list(temp)

result=True
for i in range(0,len(temp)):
    if(a.count(temp[i])==b.count(temp[i])):
        continue
    else:
        result=False

if(len(a)==len(b)):
    if(result):
        print("Permutation")
    else:
        print("No permutation")

else:
    print("No permuation")
"""


"""
permu("tech" , 3) tehc

tec
etc
ect

"""
from itertools import permutations



a,b=input("Enter the string : ").split(" ")
l=[]
for  item in permutations(a,len(b)):
    l.append("".join(item))

if(len(a)==len(b)):
    if b in l:
        print("Permutation")
    else:
        print("No permutation")

else:
    print("No permuation")


