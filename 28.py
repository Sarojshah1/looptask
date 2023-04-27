# 28. Write a for loop which print "Hello!, " plus each name in the list.
#  i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2]
#  expected output:  Hello!ram Hello!shyam
a=eval(input("enter list:"))
for i in a:
    if type(i)==str:
        print("Hello!",i)
    