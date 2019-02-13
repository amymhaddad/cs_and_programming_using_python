
# end = 6
# new_total = 0
# counter = 0

# while counter < end:
#     new_total += end
#     counter += 1

# print(new_total)


# def iterPower(base, exp):
#     result = 1

#     while exp > 0:
#         result *= base
#         exp -= 1
#     return result

# print(iterPower(2, 0))

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    i = 0

    while i < exp:
        result *= base
        i += 1
    return result

print(iterPower(2.2, 2))