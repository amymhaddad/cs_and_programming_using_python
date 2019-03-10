import random
import string

WORDLIST_FILENAME = "words.txt"


# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

lettersGuessed = []
guesses = 0
# available_letters = getAvailableLetters(lettersGuessed)

letter_dict = {}


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

secretWord = chooseWord(wordlist).lower()


def isWordGuessed(secretWord, lettersGuessed):  
    return set(lettersGuessed).issuperset(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    global letter_dict
    new_string = ''
    for letter in lettersGuessed:
        letter_dict[letter] = letter
    
    for let in secretWord:
        if let in letter_dict:
            new_string += let
        else:
            new_string += '_'
    return new_string 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabet = set(string.ascii_lowercase)
    guessed_letters = set(lettersGuessed)

    letters_not_yet_guesssed = sorted(alphabet ^ guessed_letters)
    
    return "".join(letters_not_yet_guesssed)


# def guess_a_letter(getAvailableLetters):


def hangman(secretWord, guesses, lettersGuessed):
    #increment mistakes
    #check lettersguessed

    global guesses
    word_length = len(secretWord)
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.
    print("\n")
    print("You have 8 - {guesses} left.")

    available_letters = getAvailableLetters(lettersGuessed)
    guess_one_letter = input("Please guess a letter: ")
    letter_in_word = getGuessedWord(secretWord, lettersGuessed)

###HERE: check to see if guessed letter is in secretword
#Then, call getavailableletters