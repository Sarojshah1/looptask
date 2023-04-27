# given list is [1,2,3,4] but expected output in new list [2,3,4,5]
l=[1,2,3,4]
for i in l:
    if i==1:
     l.remove(1)
     l.insert(4, 5)
print(l)    