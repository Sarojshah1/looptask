# 30. Write a for loop which appends the square of each number to the new list.
l=eval(input("enter list:"))
l1=[]
for i in l:
    a=i**2
    l1.append(a)
print(l1)