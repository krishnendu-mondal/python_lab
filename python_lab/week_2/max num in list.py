lst = []
n = int(input("Enter number of elements : "))

for i in range(n):
    ele = int(input())

    lst.append(ele)

maximum = max(lst)

print("The maximum element in this List is: ", maximum)
