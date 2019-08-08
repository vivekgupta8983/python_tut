"""
A group of code statements which can perform some specific tasks
Methods are reusable and can be called when needed in the code
"""
"""
def sum_nums(n1, n2):
    print(n1 + n2)

sum_nums(2, 8)

sum_nums(2, 5)

l = [1, 2, 3]
print(l.append(4))
print(l)

print(len(l))

"""

def sum_num(n1, n2):
     """
     get sum of two numbers
     :param n1: 
     :param n2: 
     :return: 
     """
     return n1 + n2
sum1 = sum_num(2, 8)

sum2 = sum_num(3, 3)

print(sum1)

print(sum2)
print("#"*20)

def isMetro(city):
     l = ['sfo', 'nyc', 'la']

     if city in l:
          return True
     else:
          return False

x = isMetro('boston')
print(x)
