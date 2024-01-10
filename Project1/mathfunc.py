import math
a, b, c, d = 2, 5, 3, 6
hx, hy = 8, 2
x = a * hx * b
y = c * hy * d
def func1(x, y):
       if x + y == 0:
           result = math.exp(x/2) + math.exp(y)
       else:
           result = (math.sin(x + y) + 2 * math.cos(x + y))/(x + y)

       return result
print(func1(x, y))

def func2(x, y):
    if x > y:
        result = (((x + y) ** 2) + (5 * (x - y)) + (x ** 3))/(x - y)
    else:
        result = ((2 * (x + y) ** 2) + math.exp(x - y))/(math.exp((2 * x) + (7 * y)))

    return result
print(func2(x, y))

def func3(x, y):
    if x + y == 0:
        result = math.exp(x / 2) + math.exp(y/2)
    else:
        result = (math.sin(x + y) + math.cos(x + y)) / ((2 * x) + (2 * y))

    return result
print(func3(x, y))