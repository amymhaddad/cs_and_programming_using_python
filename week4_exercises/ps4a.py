# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
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


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    # for letter in hand.keys():
    #     for j in range(hand[letter]):
    #          print(letter,end=" ")       # print all on the same line
    # print()                             # print an empty line
    hand_as_string = ''
    for letter, freq in hand.items():
    #lead with count when multiplying
        hand_as_string += freq * (letter + ' ')
    return hand_as_string


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    for letter in word:
        for dict_letter, frequency in hand_copy.items():
            if letter == dict_letter:
                hand_copy[dict_letter] = frequency -1
        
    return hand_copy


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
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

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    total_score = 0 

    # As long as there are still letters left in the hand:
    while True:
    
        # Display the hand
        print(f"Current hand: ", displayHand(hand))

        # Ask user for input
        user_word = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if user_word == '.':
            # End the game (break out of the loop)
            print(f"Goodbye! Total score: {total_score} points.") 
            break

        # elif user_word isValidWord(user_word, hand, wordList) == True and len(user_word) == n:
        #     return getWordScore(user_word, n) + 50
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
                # Reject invalid word (print a message followed by a blank line)
            if isValidWord(user_word, hand, wordList) == False:
                print("Invalid word, please try again.\n")

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                word_score = getWordScore(user_word, n)
                total_score += word_score
                print(f"{user_word} earned {word_score}. Total: {total_score} points.")
                print("\n")

                # Update the hand 
                hand = updateHand(hand, user_word)
                

# * The hand finishes when there are no more unused letters or the user
#       inputs a "."
             
                if calculateHandlen(hand) == 0:
                    print(f"Run out of letters. Total score: {total_score} points.")
                    break
    #need break to exit the loop 
            
      
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
    count_games = 0


    while True:
        user_game_choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
       
        if user_game_choice == 'e':
            break

        elif count_games == 0 and user_game_choice == 'r':
            print("You have not played a hand yet. Please play a new hand first!\n")
            count_games += 1
        
        elif (count_games > 0 and user_game_choice == 'n') or (user_game_choice == 'n'):
            current_hand = dealHand(HAND_SIZE)
            playHand(current_hand, wordList, HAND_SIZE)
            count_games += 1
            print("\n")
    
        elif count_games > 1 and user_game_choice == 'r':
            playHand(current_hand, wordList, HAND_SIZE)
            count_games += 1
        
        else:
            print("Invalid command. Try again")
            print("\n")

wordList = loadWords()
(playGame(wordList))
