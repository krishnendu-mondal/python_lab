#WAP 1st and last char of a str to upper case
text=input("Enter a string: ")
var=text.split()
res=[]
for i in var:
    result=i[0].upper() + i[1:-1]+i[-1].upper()
    res.append(result)
res=" ".join(res)
print(" "+res)