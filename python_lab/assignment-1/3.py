# WAP to check a str has atleast 1 number
string=input("Enter a string: ")

flag_l = False
flag_n = False
for i in string:
    if i in "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM":
        flag_l = True
    if i in "0123456789":
        flag_n = True
    
if flag_l and flag_n :
    print("Condition met")
else:
    print("Condition doesn't met")
