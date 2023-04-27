# 39. Given list is lst=[1,2,3,4] but print 1 and 4 only
lst=[1,2,3,4]
for i in lst:
    if i==2 or i==3:
        continue
    else:
        print(i)