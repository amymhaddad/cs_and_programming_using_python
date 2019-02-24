
import math
from decimal import Decimal

def polysum(n, s):

    area = (0.25 * n * s**2 ) / math.tan (math.pi / n)
    perimeter = s * n
    square_perimeter = math.pow(perimeter, 2)
    total = area + square_perimeter

    decimal = Decimal(total)
    decimal_output = round(decimal, 4)

    return float(decimal_output)

print(polysum(4, 2))
