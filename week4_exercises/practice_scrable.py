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

word = 'bread'
n = 5

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
    assert word in valid_word

    word_score = 0
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES[letter]
    return word_score






print(getWordScore(word, n))

