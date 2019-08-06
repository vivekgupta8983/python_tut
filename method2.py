"""
Positional Parameters
They are like optional Parameters
and can be assigned a defaults values, if no value provide from outside
"""

def sum_num(n1=2, n2=8):
    """
    get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2
sum1 = sum_num(n1=8)
print(sum1)