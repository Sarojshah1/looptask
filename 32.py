# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
# given list=[0,1,2,3,4,5,6]
l=[0,1,2,3,4,5,6]
l1=[]
for i in l:
    if i==3 or i==6:
        continue
    else:
        l1.append(i)
print(l1)

