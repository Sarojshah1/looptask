# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst.
#  Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a=eval(input("enter list:"))
b=[]
for i in a:
    b.append("dr."+str(i))
print(b)