"""
Examples to show available string method
"""
a = "1abc2abc3abc"
print(a.replace('abc', 'ABC', 1))

print(a.replace('abc', 'ABC', 2))

"""
Sub string in string
"""
sub = a[1:6]
step = a[1:6:3]

print("*********************")

print(sub)
print(step)

