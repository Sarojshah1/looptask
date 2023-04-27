# 33. Write a for loop which appends the type of each element in the first list to the second list.
a=eval(input("enter list:"))
b=[]
for i in a:
    b.append(type(i))
print(b)