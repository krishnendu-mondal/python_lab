#count the number of matching charecters
string_1=input("Enter a string_1: ")
string_2=input("Enter a string_2: ")
c=0
for i in string_1:
    if string_2.find(i) == string_1.find(i):
        c += 1
print(c)