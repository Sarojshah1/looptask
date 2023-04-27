# 7. reverse a list
a=eval(input("enter a number of list "))
reverse=[]
for i in a:
    if type(a)==list:
        reverse=[i]+reverse
    else:
        print("refresh code")
print(reverse)