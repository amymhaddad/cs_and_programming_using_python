

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break






# # Setup var on the outside of loop
# ans = 0
# neg_flag = False
# x = int(input("Enter an int: "))

# if x < 0:
#     neg_flag = True

# #Updating var inside of loop
# #This is also what's being tested (ie, ans is being updated each time only while ans**2 is less than x)
# while ans**2 < x:
#     ans = ans + 1

# if ans**2 == x:
#     print(f"The square root of {x} is {ans}.")
# else:
#     print(f"{x} isn't a perfect square.")
#     if neg_flag:
#         print(f"Did you mean -{x}?")




# s = 'abcdefgh'

# for index in range(len(s)):
#     if s[index] == 'a' or s[index] == 'u':
#         print("There's an a or u.")


# for char in s:
#     if char == 'a' or char == 'u':
#         print("There's an a or u.")


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# #why doesn't "count" get updated inside the while loop?
# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 
