# x = int(input("Enter an integer: "))
# ans = 0

# while ans**3 < abs(x):
#     ans = ans + 1 
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of", x, "is", ans)

# maxVal = int(input("Enter a positive integer: "))
# i = 0
# while i < maxVal:
#     i = i + 1
# print(i)

# x = 4 
# for j in range(x):
#     for i in range(x):
#         print(i)
#         x = 2

# x = 4
# for i in range(0, x):
#     print(i)
#     x = 5


# x = 3 
# ans = 0
# intersLeft = x

# while (intersLeft != 0):
#     ans = ans + x
#     intersLeft = intersLeft -1
# print(ans)
# print(str(x) + '*' + str(x) + ' = ' + str(ans))    


# count = 0

# for letter in 'Snow!':
#     print("Letter #" + str(count) + "is" + str(letter))
#     count += 1
#     break

# print(count)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)