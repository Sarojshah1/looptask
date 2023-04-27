# 22. Python program to calculate the sum of all the even numbers within the given range.
a=int(input("enter a range of number to print sum of even number:"))
sum=0
for i in range(a+1):
    if i%2==0:
        sum=sum+i
print(sum,"is the sum of all  even number")