# 10. Write a python program to display all the prime numbers within a given range.
# a=int(input("enter a number of range you want :"))
start=int(input("enter a number: "))
end=int(input("enter a number: "))
for i in range(start,end):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,"IS A PRIME NUMBER")
                



        
