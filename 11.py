# 11. Python program that accepts a string and calculate the number of digits and letters and space
a=input("enter a string")
b=0
c=0
d=0
for i in a:
    if i.isalpha():
        b=b+1
    elif i.isdigit():
        c=c+1
    elif i.isspace():
        d=d+1
print("total alphabet=",b)
print("total digit=",c)
print("total space =",d)