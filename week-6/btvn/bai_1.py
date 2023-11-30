from functools import reduce
def MyMultiple(*arg):
    return float(reduce(lambda x, y: x * y, arg))
print(MyMultiple(1, 2, 3, 4))
print(MyMultiple(5, 5, 5))
print(MyMultiple(1.2, 5))
