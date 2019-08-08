"""
This is Example of built-in Method help to manipulate the string
"""

cars = ["bmw", "honda", "audi"]
lenght = len(cars)
print(lenght)

cars.append("Benz")              ## it adds the value on the ends of lists
print(cars)

cars.insert(1, "Jeep")          ## it insert the values in the list as we defined on it
print(cars)

cars.insert(0, "Thar")
print(cars)

x = cars.index("audi")
y = cars.index("Thar")
print(y)
print(x)

cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)


print("*#"*20)
print(cars)

cars.sort()

print(cars)