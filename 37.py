# 37. Python program to count the number of even and odd numbers from a series of numbers.  
a=int(input("enter a range of number to print sum of odd number:"))
b=0
c=0
for i in range(a+1):
    if i%2!=0:
        b +=1
    else:
        c+=1
print(" the total number of   odd number is",b)
print(" the total number of   even number is",c)