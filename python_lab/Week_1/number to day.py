day=int(input('Enter a Positive integer between 1 to 7: '))
if day >= 1 and day <=7 :  
    if day==1:
        print('Monday')
    elif day==2:
        print('Tuesday')
    elif day==3:
        print('Wednesday')
    elif day==4:
        print('Thursday')
    elif day==5:
        print('Friday')
    elif day==6:
        print('Saturday')
    else:
        print('Sunday')
else:
    print('Invalid Input')