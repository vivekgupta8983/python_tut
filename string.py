"""
Example of String works in Python
Sequence of characters
Contians a-z, 0-9, @
In double or Single quotes
"""
a = "This is simple string"
b = 'Using single quotes'

print(a)
print(b)

c =  "need to use 'qoutes' inside the string"
print(c)

d = "Another way to handle \"qoutes\""
print(d)


"""
Accessing character in a string
"""
first = "nyc"[0]
city = "cyn"
print(first)
ft = city[0]
print(ft)


"""
len()
lower()
upper()
str()
"""

stri = "This is Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + " hello " + "" + " world")
print("first" + " " + "city")