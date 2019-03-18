import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

word = 'apple'
n = 7

def loadWords():
    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList



#deals a hand of random vowels and constanents
#Pass in "n" which is the number of letters to generate for the hand, which consists of V's and C's
def dealHand(n):
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand

hand = dealHand(n)

#displays hand with spaces between each letter: w a y b i l l 
#Need to use dealHand as a helper function in displayHand. This is why we set it to a variable and pass it into displayHand.
#We are taking the dictionary that results from dealHand and displaying it in the function bel0w.
def displayHand(hand):
    updateHand(hand, word)
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")        
    print()                         

user_hand = displayHand(hand)


#getFrequencyDict takes in a string, so pass in display_hand
#shows frequency of each letter that occurs in a hand
# def getFrequencyDict(sequence):
#     sequence = displayHand(hand)
#     freq = {}
#     for x in sequence:
#         freq[x] = freq.get(x,0) + 1
#     return freq

# print(getFrequencyDict(user_hand))

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


def updateHand(hand, word):
    copy_dict = hand.copy()
    for letter in word:
        for key, value in copy_dict.items():
            if letter in key:
                copy_dict[key] = value -1
        
    return copy_dict

print(updateHand(hand, word))
        
