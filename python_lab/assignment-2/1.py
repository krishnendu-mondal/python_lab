num = int(input())
if (num > -10**6 and num < 10**6):
    if (num % 2 == 0):
        print(num+2)
    else:
        print(num+1)
