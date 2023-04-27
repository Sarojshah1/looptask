# 15. program to check given number is palindrome or not
a=int(input("enter a number "))
temp=a
sum=0
while a>0:
    b=a%10
    sum=(sum*10)+b
    a= a//10
if sum == temp:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")