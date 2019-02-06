
# user_number = int(input("Please think of a number between 0 and 100!"))

print("Please think of a number between 0 and 100!")
# user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
low = 0
high = 100
guess = (low + high) // 2

while low <= high:
    print("Is your secret number "+ str(guess)+ "?")
    guess_evaluation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

#Always check for validity first b/c otherwise it can get trapped. 

#Don't need these first conditionals b/c it's the user who decides whether or not the number is high or low or correct
#What i'm testing wtih the conditionals below is what to do based on the user input. 
##
    # if guess == secret_number:
        if guess_evaluation == 'c':
            print("Game over. Your secret number was:", guess)
            break
        else:
            print("Sorry, I did not understand your input.")
    
    elif guess > secret_number:
        if guess_evaluation == 'h':
            high = guess
        else:
            print("Sorry, I did not understand your input.")
        
    else:
        if guess_evaluation == 'l':
            low = guess 
        else:
            print("Sorry, I did not understand your input.")
       
    guess = (low + high) // 2
