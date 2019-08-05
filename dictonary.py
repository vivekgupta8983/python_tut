"""
Data type to store more than one value in one variable name, in term of key value pairs
Dictionary items are in brackets {} in key:value pairs separated with "," {'k1:v1, k2:v2}
no sequencing, no indexing in dictionary ---> MApping
"""

car = {'make': 'BMW', 'model':'500i', 'years':'20016'}
print(car)

d = {}

model = car['model']
print(car['model'])
print(model)

d['one'] = 1
d['two'] = 2
print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)

d['two'] = d['two'] + 8
print(d)
