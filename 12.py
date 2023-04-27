# 12. Python program to check the validity of username and password input by users
username1="saroj09"
password1="saroj0777"
for i in range(3):
    username = input("enter your username:")
    password = input("enter your password:")
    if username==username1 and password==password1:
        print("sucessfully log in")
    elif i==2:
        print("you are blocked")
    else:
        print(f"you have{3-(i+1)} attempt left")