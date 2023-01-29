f = open("budget.txt", "w")
f.write("Todays budget is potato 5 kg @Rs 30 and Rice 2 Kg @Rs 75 and vegetables 1 kg @ Rs 200 including additional items")

f = open("expense.txt", "w")
f.write("Today spent Rs 135 in potato, Rs 150 in Rice and Rs 170 in vegetables")

f = open("budget.txt", "r")
content1 = f.read()

result1 = [int(i) for i in content1.split() if i.isdigit()]

amount = result1[1::2]
price  = result1[0::2]

budget_list = []
for i in range(0, len(amount)):
    budget_list.append(amount[i] * price[i])

budget = 0
for i in range(0, len(budget_list)):
    budget = budget + budget_list[i]
print ("The budget is:",budget)

f = open("expense.txt", "r")
content2 = f.read()
result2 = [int(i) for i in content2.split() if i.isdigit()]
expense = 0
for i in result2:
    expense += i
print("The expense is:", expense)

if budget>expense:
    print("Expense",str(expense) + " is within Budget",str(budget))