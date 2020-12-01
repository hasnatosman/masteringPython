numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)
"""
odd = [i for i in numbers if i % 2 != 0]
print(odd)

sqr_num = [i * i for i in numbers]
print(sqr_num)
