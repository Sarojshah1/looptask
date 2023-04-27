# 13. program to print the given number is odd or even
a=int(input("enter a number:"))
for i in range(1,a+1):
    if a%2==0:
        print(a,"even number")
        break
    else:
        print(a,"is odd number")
        break