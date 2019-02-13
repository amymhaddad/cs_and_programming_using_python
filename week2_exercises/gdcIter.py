
#Write an iterative function that finds the greatest common divisor of 2 positive integers.

a = 8
b = 12
test_val = 0

if a < b:
    test_val = a
elif a > b:
    test_val = b

highest_val = max(a, b)

for number in range(test_val+1):
    if highest_val % test_val == 0:
        print(test_val)
        break
    else:
        test_val -= 1
