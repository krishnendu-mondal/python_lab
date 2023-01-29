#count the number of vowels
string=input("Enter string:")
string=string.lower()
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels += 1
print("Number of vowels are:",vowels)
