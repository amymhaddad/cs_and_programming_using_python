
# user_number = int(input("Please think of a number between 0 and 100!"))

print("Please think of a number between 0 and 100!")
secret_number = 42
low = 0
high = 100
guess = (low + high) // 2

while low <= high:
    print("Is your secret number "+ str(guess)+ "?")
    guess_evaluation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if guess == secret_number:
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
