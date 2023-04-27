# 9. given number is prime or not
a=int(input("enter a number:"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,"is not prime number")
            break
        else:
            print(a," is  a prime")
            break
else:
    print("please enter a number greater than 1")