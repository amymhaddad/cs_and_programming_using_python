#Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
#You should use the square procedure that you defined in an earlier exercise (you don't need to redefine square in this box; when you call square, the grader will use our definition).

def square(number):
    '''
    x: int or float.
    '''
    return number * number

# square(3)

def fourthPower(x):
    '''
    x: int or float.
    '''
    # square(x)
    return square(x) * square(x)

print(fourthPower(2))
