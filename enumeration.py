# x = int(input("Enter an integer: "))
# ans = 0

# #setup comparison and test statement in while loop
# #the while loop is generating guesses
# while ans**3 < x:
#     #increment by 1
#     ans = ans + 1

# #The while loop keeps generating guesses until it gets to the right thing OR it's gone too far
# #Then, I check -- with the conditionals below -- to see which case I'm in
# #The "if" below is declarative knowledge: do I have a cubed root?
# if ans**3 != x:
#     print(x, "is not a perfect cube")
# else:
#     print("Cube root of", x, "is", ans)

#challenge with code above is that it only works for positive ints



# x = int(input("Enter an integer: "))
# ans = 0

# while ans**3 < abs(x):
#     ans = ans + 1

# #check the cube root against abs value of x
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     #The code below is where I decide if I want the neg or positive version 
#     if x < 0:
#         ans = -ans 
#     print("Cube root of", x, "is", ans)


#cube = the thing I'm trying to find the cube root of (ie, what number is multiplied 3x to get 8)
#use for loop: I know that the number must be less than cube itself
# cube = 27
# for guess in range(cube + 1):
#     if guess**3 == cube:
#         print("Cube root of", cube, "is", guess)


cube = -27
for guess in range(abs(cube + 1)):
    #the conditional below checks if I've gone too far (note: >=)
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    #if perfect cube, I'm determining if I want the positive or negative version of it
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + "is " + str(guess))


