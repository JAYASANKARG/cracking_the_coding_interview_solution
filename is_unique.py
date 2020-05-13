"""Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures clear

"""
"""s=input("Enter the string : ")
before_set=len(s)
s=set(s)
after_Set=len(s)
if(before_set==after_Set):
    print("all is unique")
else:
    print("Not unique")

o(1)

result=True
s=input("Enter the string : ")
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            result=False
            break
if(result):
    print("unqiue")
else:
    print("Not unique")
o(n2)->n*n
"""

"""Bitwise operator
a=0,b=1,c=2
a=97
b=98


"""

def unique(s):
    flag=0
    for i in range(len(s)):
        temp=ord(s[i])-ord('a')
        if(flag & (1<<temp)>0):
            return False
        flag |=1<<temp
    return True

s=input("enter the string : ")
if(unique(s)):
    print("unique")
else:
    print("not unique")