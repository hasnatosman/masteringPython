exp = [200, 400, 600, 800]
total = 0

for i in range(len(exp)):
    print('Month', (i+1), 'Expense is: ', exp[i])
    total = total + exp[i]
print('Total expenses :', total)