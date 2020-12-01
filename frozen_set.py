# set is an unordered collection of unique elements

num = [1, 3, 5, 7, 4, 2, 9, 1]
unique_num = set(num)
print(unique_num)
unique_num.add(8)
print(unique_num)

# set can add elements where frozen set can;t add or anything

fs = frozenset(num)
print(fs)
"""
fs.add(6)
print(fs)
"""

x = 1 in num
print(x)
y = 6 in num
print(y)

for i in num:
    print(i)

x = {'a', 'b', 'c'}
y = {'c', 'd', 'f', 'g'}
union = x | y
print(union)
intersection = x & y
print(intersection)