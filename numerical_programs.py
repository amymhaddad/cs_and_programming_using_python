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


# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!') 

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 

# num = 10
# print('Hello')

# while num >= 2:
#     print(num)
#     num -= 2
#     break
 
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))