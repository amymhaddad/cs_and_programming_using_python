# def multi_iterations(a, b):
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result

# print(multi_iterations(4, 2))

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

print(mult(4, 3))