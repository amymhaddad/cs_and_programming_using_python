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
x = -25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

low = 0.0
high = max(1.0, x)
ans = (high + low) / 2

while abs(ans**2 - x) >= epsilon:
    print(f"Low = {low} High = {high} Ans = {ans}")
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else: 
        high = ans
    ans = (high + low) / 2.0

print(f"Number of guesses: {numGuesses}")
print(f"{ans} is close to the sq root of {x}")
