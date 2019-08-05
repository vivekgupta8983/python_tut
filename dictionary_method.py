"""
Dictionary Methods
"""

car = {'make': 'BMW', 'model':'500i', 'years':'20016'}
cars = {'BMW':{'model':'550i', 'years':'2016'}, 'benz':{'model':'E350','years':'2015'}}

print(car.keys())
print(cars.values())
print(car.values())
print(car.keys())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)

print(car.clear())
print(car)