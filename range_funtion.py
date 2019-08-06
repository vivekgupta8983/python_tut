"""
Built-in function
Create a sequence of number but does not save them in memory
very useful for generating numbers
"""

a = range(3, 30, 3)
print(a)
print(type(a))

print(list(a))


for num in range(1, 10, 3):
    print(num)
