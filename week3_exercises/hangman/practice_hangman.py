import random
import string

WORDLIST_FILENAME = "words.txt"

lettersGuessed = []

def loadWords():
    print("Loading word list from file...")

    with open(WORDLIST_FILENAME) as f_object:
        contents = f_object.readline() 
    wordlist = contents.split()
    print(" ", len(wordlist), "words loaded.")
    
    return contents

wordlist = loadWords()

def chooseWord(wordlist):
    return random.choice(wordlist)

secretWord = chooseWord(wordlist).lower()


def isWordGuessed(secretWord, lettersGuessed):  
    return set(lettersGuessed).issuperset(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    global letter_dict
    new_string = ''
    
    for let in secretWord:
        if let in lettersGuessed:
            new_string += let + ' '
        else:
            new_string += '_' + ' '
    return new_string 


def getAvailableLetters(lettersGuessed):
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set(lettersGuessed)
    letters_not_yet_guesssed = sorted(alphabet ^ guessed_letters)
    
    return "".join(letters_not_yet_guesssed)


def guess_a_letter():
    global lettersGuessed

    guess_one_letter = input("Please guess a letter: ")
    guess_in_lowercase = guess_one_letter.lower()
    lettersGuessed.append(guess_in_lowercase)
    get_guessed_word = getGuessedWord(secretWord, lettersGuessed)

    if guess_in_lowercase not in secretWord:
        result = (f"Oops! That letter is not in my word: {get_guessed_word}")
    elif lettersGuessed.count(guess_in_lowercase) > 1:
        result = (f"You've already guessed that letter: {get_guessed_word}")
    elif guess_in_lowercase in secretWord:
        result = (f"Good guess: {get_guessed_word}")
    return result


def hangman(secretWord):
    global lettersGuessed
    word_length = len(secretWord)
    available_letters = getAvailableLetters(lettersGuessed)
    
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.")
    print("\n")

    total_guesses = 8
    while total_guesses <= 8 or "_" in secretWord:
        get_guessed_word = getGuessedWord(secretWord, lettersGuessed)
        completed_word = get_guessed_word.replace(" ", "")
            
        if total_guesses == 0:
            print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
            break
        elif completed_word == secretWord:
            print("Congratulations, you won!")
            break
        else:
            print(f"Available letters: {available_letters}")
            print(guess_a_letter())
            print("\n")
            total_guesses -= 1
            print(f"You have {total_guesses} guesses left.")

print(hangman(secretWord))