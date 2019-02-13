
# def iterPower(base, exp):
#     result = 1

#     for i in (range(exp)):
#         result *= base
#     return result

# print(iterPower(4, 4))

def iterPower(base, exp):
    result = 1

    while exp > 0:
        result *= base
        exp -= 1
    return result

print(iterPower(2, 3))