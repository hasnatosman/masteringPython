s = set([1, 2, 3, 4, 5, 3, 2])
print(s)
even = {i for i in s if i % 2 == 0}
print(even)
odd = {a for a in s if a % 2 != 0}
print(odd)
square = {x * x for x in s}
print(square)