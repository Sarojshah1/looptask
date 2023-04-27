# 38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only
lst=[1,2,3,4]
for i in lst:
    if i==3:
        continue
    else:
        print(i)