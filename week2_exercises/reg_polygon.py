
import math
from decimal import Decimal

def polysum(n, s):
    sides_squared = math.pow(s, 2)
    tan = math.tan
    pi = math.pi

    area = (0.25 * n * sides_squared) / tan(pi / n)
    perimeter = s * n
    square_perimeter = math.pow(perimeter, 2)
    total = area + square_perimeter

    decimal = Decimal(total)
    decimal_output = round(decimal, 4)

    return float(decimal_output)

print(polysum(87, 84))