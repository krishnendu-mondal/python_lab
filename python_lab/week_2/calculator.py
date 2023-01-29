choice=input('Enter your choice among these( +, -, *, /, ^ ):    ')
if choice=='+':
    a=int(input())
    b=int(input())
    sum=a+b
    print(sum)
elif choice=='-':
    a=int(input())
    b=int(input())
    sub=a-b
    print(sub)
elif choice=='*':
    a=int(input())
    b=int(input())
    mul=a*b
    print(mul)
elif choice=='/':
    a=int(input())
    b=int(input())
    div=a/b
    print(div)
else:
    print("Invalid choice! Please select from given choice...")
