# String are used to store text data.


text = 'ice cream'
print(text)
print(text[0])
print(text[0:3])
print(text[4:])

# string are immutable , once you create them , you can't change them.

s1 = 'Hello'
s2 = 'World'
s = s1 + ' '+ s2
print(s)

# you can't add a string with a number in python.
name = 'Hasnat'
age = 25
print(name + ' is'+' ' + str(age) + ' years old.')