# 17. Python program to check a number is perfect square
a=eval(input("enter a number"))
sq=False
for i in range(1,a//2+1):
    if i*i==a:
        sq=True
        break
if sq:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")