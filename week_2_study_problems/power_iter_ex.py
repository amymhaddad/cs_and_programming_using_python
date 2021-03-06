
#Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. 
# For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

#Solution 1
def iterPower(base, exp):
    result = 1

    for i in (range(exp)):
        result *= base
    return result

print(iterPower(4, 4))

#Solution 2
def iterPower(base, exp):
    result = 1

    while exp > 0:
        result *= base
        exp -= 1
    return result

print(iterPower(2, 3))