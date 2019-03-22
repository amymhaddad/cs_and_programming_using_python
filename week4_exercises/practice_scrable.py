
#Sum the values of the hand (ie the number of letters available to use). 
#We will use this info as a check to see when we need to end the game (ie, no more letters to use)
def calculateHandlen(hand):
    return sum(hand.values())


def updateHand(hand, word):
    hand_copy = hand.copy()
    for letter in word:
        for dict_letter, frequency in hand_copy.items():
            if letter == dict_letter:
                hand_copy[dict_letter] = frequency -1
        
    return hand_copy


def getWordScore(word, n):
    valid_word = loadWords()
    word_score = 0

    if word not in valid_word:
        return word_score
    
    else:
        for letter in word:
            word_score += (SCRABBLE_LETTER_VALUES[letter]) * len(word)
        if len(word) == n:
            word_score += 50

    return word_score 



def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False

    hand_copy = hand.copy()

    for letter in word:
        if letter not in hand.keys():
            return False
        else:
            for dict_letter, frequency in hand_copy.items():
                if letter == dict_letter:
                    hand_copy[dict_letter] = frequency -1        
            for frequency in hand_copy.values():
                if frequency < 0:
                    return False    
    return True



def displayHand(hand):
    hand_as_string = ''
    for letter, freq in hand.items():
        hand_as_string += freq * (letter + ' ')
    return hand_as_string





def playHand(hand, wordList, n):
    #score variable on outside of loop that'll update in the while loop
    total_score = 0 

    #while the condition is true, do the following:
    while True:
        #Display the current hand (shows all of the available letters)
        print(f"Current hand: ", displayHand(hand))
        #ask for user to enter a word or exit the game
        user_word = input('Enter word, or a "." to indicate that you are finished: ')
        
        #IF user wants to end game, then end it and return total socre
        #exit the while loop by using a break statement
        if user_word == '.':
            print(f"Goodbye! Total score: {total_score} points.") 
            break

        #IF the user doens't want to end the game and has entered a word, we need to see if the word is valid or not
        else:
            #Check if the word is valid by calling the function isValidWord.
            #Notice that I needed to update the parameters I pass into isValidWord -- I pass in user_word (which is the word the user inputted) instead of "word"
            if isValidWord(user_word, hand, wordList) == False:
                print("Invalid word, please try again.\n")
           
            #Word MUST be valid (based on the check above) so we enter the "else" clause
            else:
                #Get the score for the valid word by calling getWordScore
                word_score = getWordScore(user_word, n)

                #add the score for this word to total_score and print the score
                total_score += word_score
                print(f"{user_word} earned {word_score}. Total: {total_score} points.")
                print("\n")
                
                #Update the hand based on the letters used to form the word. Returns an updated dictionary that I'm setting = to the variable "hand"
                hand = updateHand(hand, user_word)
                
                #Check to see if the length of the hand is 0, which means we're out of letters. If len(hand) is 0 then end the game
                if calculateHandlen(hand) == 0:
                    print(f"Run out of letters. Total score: {total_score} points.")
                    break

def playGame(words):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    #variable on the outside of the while loop that'll be incremented inside the while loop
    count_games = 0

    #keep running this while loop until a condition is False
    while True:
        #get user input and react based on input
        user_game_choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        #End the game if user enters "e"
        if user_game_choice == 'e':
            break

        #using a counter to see if this is the first time a user plays a game and tries to do something other than start a new game
        elif count_games == 0 and user_game_choice == 'r':
            print("You have not played a hand yet. Please play a new hand first!\n")
            count_games += 1
        
        #Ready to start a new game and call functions 
        elif (count_games > 0 and user_game_choice == 'n') or (user_game_choice == 'n'):
            #dealHand is assigned to current_hand. It stays in memory unless it's reassigned
            #Use a variable here b/c dealHand returns something and we need to use dealHand elsewhere (ie, in the PlayHand function call)
            current_hand = dealHand(HAND_SIZE)
            #Calling function playHand --> playHand has no return value so I can just call it -- I don't need to assign it to a variable.
            playHand(current_hand, wordList, HAND_SIZE)
            count_games += 1
            print("\n")
            
        #If the user wants to REPEAT the previously played game (from the elif above)
        elif count_games > 1 and user_game_choice == 'r':
            #I need to re-call playHand from the condition above. This works b/c playHand isn't assigned to a variable that's been updated.
            #Instead the playHand stays the same throughout the entire iteration through the while loop. 
            #In other words, everything (ie, dealHand and playHand) stay the same from the condition above

            #play_hand has no return value so I don't need to use a variable when I call this function (it's a side effect). 
            #It does something for me, there's no output value

            playHand(current_hand, wordList, HAND_SIZE)
            count_games += 1
        
        else:
            print("Invalid command. Try again")
            print("\n")

wordList = loadWords()
(playGame(wordList))


#a while loop inside a while loop
def playGame(wordList):

    count_games = 0

    while True:
        game_type_choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        game_type_choice_options = ['n', 'r', 'e']
        valid_game_type_choice = (game_type_choice == 'n') or (game_type_choice == 'r' and count_games > 0) or (count_games > 0 and game_type_choice == 'n')
        game_opponent_options = ['c', 'u']

        if game_type_choice == 'e':
            break
        
        elif game_type_choice not in game_type_choice_options:
            print("Invalid command. Try again")
            print("\n")
        
        elif count_games == 0 and game_type_choice == 'r':
            print("You have not played a hand yet. Please play a new hand first!\n")
            count_games += 1

        while valid_game_type_choice:
            game_opponent_input = input("Enter u to have yourself play, c to have the computer play: ")
            count_games += 1

            if game_opponent_input == 'u' and game_type_choice == 'n':
                current_hand = dealHand(HAND_SIZE)
                playHand(current_hand, wordList, HAND_SIZE)
                print("\n")
                break

            elif game_opponent_input == 'u' and game_type_choice == 'r':
                playHand(current_hand, wordList, HAND_SIZE)
                break
    
            elif game_opponent_input == 'c' and game_type_choice == 'n':
                current_hand = dealHand(HAND_SIZE)
                compPlayHand(current_hand, wordList, HAND_SIZE)
                print("\n")
                break
            
            elif game_opponent_input == 'c' and game_type_choice == 'r':
                compPlayHand(current_hand, wordList, HAND_SIZE)
                break
                   
            elif game_opponent_input not in game_opponent_options:
                    print("Invalid command. Try again")
                    print("\n")
