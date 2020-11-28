"""
In computer science, a list or sequence is an abstract(is an idea or thought that has no physical existence)
 data type that represents a countable number of ordered values, where the same value may occur more than once..

"""

item = ['a', 'b', 'c']
print(item)
print(item[0])
print(item[1:])

# list data structure is mutable.

item.append('d')
print(item)

# we can insert anywhere we want

item.insert(0, 'A')
print(item)

# we can add two list together.

list1 = ['1', '2', '3']
list2 = ['4', '5']
new_list = list1 + list2
print(new_list)
print(len(new_list))
