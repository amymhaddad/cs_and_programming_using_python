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
    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

word = 'waybill'
n = 7

# def getFrequencyDict(sequence):
#     """
#     sequence: string or list
#     return: dictionary of number of times each letter occurs in the given sequence
#     """
#     freq = {}
#     for x in sequence:
#         freq[x] = freq.get(x,0) + 1
#     return freq

#{'b': 1, 'r': 1, 'e': 1, 'a': 1, 'd': 1}

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
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


