"""
For loop example for Python
"""
# string for loop
my_string = 'abcabc'
for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print()

# List for loops
cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car)

nums = [1, 2, 3]
for n in nums:
    print(n * 10)
# dictionary for loops
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + " " + str(d[k]))


print("#"*20)

for k,v in d.items():
    print(k)
    print(v)
