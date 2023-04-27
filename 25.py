# 25. Multiplication of a list
a=eval(input("enter list:"))
for i in a:
    print("Multiplication of",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)