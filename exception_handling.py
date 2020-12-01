x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

try:
    z = x / y
except ZeroDivisionError as e:
    print('Division by zero exception.')
    z = None
print('Division is: ', z)