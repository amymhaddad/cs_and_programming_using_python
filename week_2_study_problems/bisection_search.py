
# iteration = 0
# while iteration < 5:
#     count = 0
#     print(f"Count after assignment: {count}")
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

#cube ex from video lecture 

# cube = 29
# epsilon = 0.01
# guess = 0.0
# increment = 0.01
# num_guesses = 0

# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
# print('num_guesses =  ', num_guesses)

# if abs(guess**3 - cube) >= epsilon:
#     print("failed on cube root of ", cube)
# else:
#     print(guess, "is close to the cube root of", cube)

x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print(f"Low = {low} and High = {high} and Ans = {ans}")
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
        # print(high)
    ans = (high + low) / 2.0







#The program below cycles through ALL numbers for x

# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0

# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     numGuesses += 1
# print(f"Number of guesses: {numGuesses}")

# if abs(ans**2 - x) >= epsilon:
#     print(f"Failed sq root of {x}")
# else:
#     print(f"{ans} is close to the sq root of {x}")



#The program below cuts the search in half each time 
# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0

# low = 0.0
# high = max(1.0, x)
# ans = (high + low) / 2

# while abs(ans**2 - x) >= epsilon:
#     print(f"Low = {low} High = {high} Ans = {ans}")
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else: 
#         high = ans
#     ans = (high + low) / 2.0

# print(f"Number of guesses: {numGuesses}")
# print(f"{ans} is close to the sq root of {x}")
