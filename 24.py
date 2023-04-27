# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]
l=[1,2,3,4]
l1=[]
for i in range(4):
    a=l[i]**3
    l1.append(a)
print(l1)