# 36. removal bad characters from the given string.
#  Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n". 
#  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"," "]
string = "py;th* o:n ! ;py * t*h:o !n"
b=""
for i in string:
    if i not in bad_chars:
        b += i
print(b)