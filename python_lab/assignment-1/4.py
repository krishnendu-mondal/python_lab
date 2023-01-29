#only if vowels are present
string=input("Enter a string: ")
string=string.lower()
flag_l = False
for i in string:
    if i not in "aeiou":
        flag_l = True
if flag_l :
    print("Condition doesn't met")
else:
    print("Condition met")