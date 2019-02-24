#Use recursion to find the greatest common divisor of two positive integers

def gcdRecur(a, b):
    biggest_num = max(a, b)
    smallest_num = min(a, b)
    
    if biggest_num == 0:
        return smallest_num
    elif smallest_num == 0:
        return biggest_num
    else: 
        remainder = biggest_num % smallest_num
        return gcdRecur(smallest_num, remainder)

print(gcdRecur(12, 45))
