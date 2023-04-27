# 40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst=[1,2,3,4]
for i in range(4):
    if i==3:
        lst.remove(3)
        lst.insert(1, "a")
print(lst)
