# 23. Python program to count the space of a given string
a=input("enter a string")
count=0
for i in a:
    if i.isspace():
        count+=1
print("total space is",count)