# WAP to print upper case for half of the input str
text=input("Enter a string: ")
length=len(text)
if length%2==0:
    length=(length//2)
else:
    length=(length//2)+1

res=text[0:length].upper()+text[length:]

print(res)
