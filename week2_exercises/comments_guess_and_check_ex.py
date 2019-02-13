
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high) // 2

while low <= high:
    print("Is your secret number "+ str(guess)+ "?")
    guess_evaluation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

#Always check for validity first, as I'm doing below. Otherwise, I'll never hit the test condition.
    if guess_evaluation != "c" or guess_evaluation != "h" or guess_evaluation != 'l':
        print("Sorry, I did not understand your input.")

#Don't need these first conditionals (ie, if guess == secret_number) b/c it's the user who decides whether or not the number is high or low or correct
#What I need to test is what to do based on the user input. (ie, if the user enters "c")


    if guess == secret_number:
        if guess_evaluation == 'c':
            print("Game over. Your secret number was:", guess)
            break
        else:
            print("Sorry, I did not understand your input.")

#Need to remove first conditional below  
    elif guess > secret_number:
        if guess_evaluation == 'h':
            high = guess
        else:
            print("Sorry, I did not understand your input.")

#Need to remove first conditional below     
    else:
        if guess_evaluation == 'l':
            low = guess 
        else:
            print("Sorry, I did not understand your input.")
       
    guess = (low + high) // 2
