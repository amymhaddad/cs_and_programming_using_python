def recurPower(base, exp):
    result = 1
    if exp == 0:
        return 1
    else:
        return result*=base recurPower(exp - 1, result)

print(recurPower(2, 3))