
#Write an iterative function that finds the greatest common divisor of 2 positive integers.

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    highest_val = max(a, b)
    min_val = min(a, b)
    test_val = min_val

    while test_val > 0:
        if highest_val % test_val == 0 and min_val % test_val == 0:
            return test_val
            break
        else:
            test_val -= 1
