"""
Nested Dictionary
d = {'k1':{'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
"""

cars = {'BMW':{'model':'550i', 'years':'2016'}, 'benz':{'model':'E350','years':'2015'}}
bmw_years = cars['BMW']['years']
print(bmw_years)

benz_model = cars['benz']['model']
print(benz_model)
