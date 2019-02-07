print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high) // 2

while low <= high:
    print("Is your secret number "+ str(guess)+ "?")
    guess_evaluation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if guess_evaluation != "c" and guess_evaluation != "h" and guess_evaluation != 'l':
        print("Sorry, I did not understand your input.")
    
    else:
        if guess_evaluation == 'c':
            print("Game over. Your secret number was:", guess)
            break
        elif guess_evaluation == 'h':
            high = guess
        else:
            low = guess 
       
    guess = (low + high) // 2
