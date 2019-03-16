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

sequence = 'wayybill'
n = 7

def getFrequencyDict(sequence):
    """
    sequence: string or list
    return: dictionary of number of times each letter occurs in the given sequence
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


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



#displays hand with spaces between each letter: w a y b i l l 
def displayHand(hand):
    hand = getFrequencyDict(sequence)

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")        
    print()                         
    

#returns random vowels and constanents
def dealHand(n):

    #iterate through the number of vowels (based on calc from numbVowels).
    for i in range(numVowels):
        vowel = VOWELS[random.randrange(0,len(VOWELS))]
        hand[vowel] = hand.get(vowel, 0) + 1

    #start with numVowels and end at "n". This will determine the number of constants we need.
    for i in range(numVowels, n): 
        constanant = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[constanant] = hand.get(constanant, 0) + 1

    return hand


def updateHand(hand, word):
    #1. make sure displayHand and dealHand work 
    #2. Call dealHand in this function
    #3. Write out this fucntion

   
    # Aim: create a word, remove letters from hand, and return leftover letters
    # try using set

    #given a hand (ie, a dictionary)
    #given a word (ie, a string)
    #This function uses the letters from "hand" to spell a word --->This is the algo I write
    ###make a copy of hand 
    ### extract letters in "word" from "copied_hand"  -->ie, delete these values --> return leftover values

    #Returns a COPY of hand with only the remaining letters 