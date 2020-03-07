import math
def find_roots(a, b, c):
    first = (-1*b) + math.sqrt(math.pow(b, 2) - (4*a*c))
    first = first / (2*a)
    second = (-1*b) - math.sqrt(math.pow(b, 2) - (4*a*c))
    second = second / (2*a)
    roots_tuple = (first,second)
    return roots_tuple

print(find_roots(2, 10, 8))