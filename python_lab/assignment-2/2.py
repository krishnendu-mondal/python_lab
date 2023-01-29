string = input()
if string.islower() and string.isalpha():
    string = string.split()
    for i in string:
        count = 0
        for j in range(len(i)-1):
            if i[j] < i[j+1]:
                count += 1
        print(count, end="")
