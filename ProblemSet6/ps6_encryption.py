# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()
##print getStoryString()

# (end of helper code)
# -----------------------------------
#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
    shift: 0 <= int < 26
    returns: dict
    """
    letter = []
    for low in string.ascii_lowercase:
        letter.append(low)
##    for upper in string.ascii_uppercase:
##        letter.append(upper)

    numKeyDict = {}
    num = 1
    for letter1 in letter:
        numKeyDict[num] = letter1
        num += 1

    letterKeyDict = {}
    numNew = 1
    for letter2 in letter:
        letterKeyDict[letter2] = numNew
        numNew += 1    
       
    newDict = {}
    for original in letterKeyDict:
        originalVal = letterKeyDict[original]
        if originalVal + shift > 26:
            originalVal -= 26
        newDict[original] = numKeyDict[originalVal+shift]
        newDict[original.upper()] = numKeyDict[originalVal+shift].upper()
    return newDict

##print buildCoder(9)
#Inspired by
#https://github.com/jdhuasirui/MITx--CMITx--6.00.1x-Introduction-to-CS-and-Programming-Using-Python/blob/master/Problem%20Set%206.py
##def buildCoder(shift):
##    coder = {}
##    for i in range(len(string.ascii_lowercase)):
##        s = (i + shift) % 26
##        c = string.ascii_lowercase[i]
##        sc = string.ascii_lowercase[s]
##        coder[c] = sc
##        coder[c.upper()] = sc.upper()
##    return coder        

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = []
    for i in text:
        if i in string.punctuation or i ==' ' or i in string.digits:
            result.append(i)
        else:
            result.append(coder[i])
    result = ''.join(result)
    return result
##print applyCoder("Hello, world!", buildCoder(3))
##print applyCoder("Khoor, zruog!", buildCoder(23))

## Solution 2
##def applyCoder(text, coder):

##    result = ""
##    for c in text:
##        if c in string.punctuation or c == ' ' or c.isdigit():
##            result += c
##        else:
##            result += coder[c]
##    return result

##>>> applyCoder("Hello, world!", buildCoder(3))
##'Khoor, zruog!'
##>>> applyCoder("Khoor, zruog!", buildCoder(23))
##'Hello, world!'  

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

##>>> applyShift('This is a test.', 8)
##'Bpqa qa i bmab.'
##>>> applyShift('Bpqa qa i bmab.', 18)
##'This is a test.'
#

# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxNum = 0
    bestShift = 0
    shStr = ''
    wordCount = 0

    def split(text):
        ex = string.punctuation + string.digits
        for i in text:
            if i in ex:
                text = text.replace(i,'')
        return text.split(' ')

    for shift in range(26):
        shStr = applyShift(text, shift)
        strList = split(shStr)

        for word in strList:
            if isWord(wordList, word):
                wordCount += 1
                
        if wordCount > maxNum:
            maxNum = wordCount
            bestShift = shift

    return bestShift

##wordList = loadWords()
##story = getStoryString()
####print story
##print findBestShift(wordList, 'getStoryString()')

##>>> s = applyShift('Hello, world!', 8)
##>>> s
##'Pmttw, ewztl!'
##>>> findBestShift(wordList, s)
##18
##>>> applyShift(s, 18)
##'Hello, world!'

##Test:
##wordList = loadWords()
##print findBestShift(wordList, 'Pmttw, ewztl!')

##Solution 2
##def findBestShift(wordList, text):
##    text_words = text.split(" ")
##    max_valid = 0
##    best_shift = 0
##    for shift in range(26):
##        num_valid = 0
##        for word in text_words:
##            original = applyShift(word,shift)
##            if isWord(wordList, original):
##                num_valid += 1
##        if num_valid > max_valid:
##            max_valid = num_valid
##            best_shift = shift
##    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    
    story = getStoryString()
    wordList = loadWords()
    shiftNum = findBestShift(wordList, story)
    return applyShift(story, shiftNum)
##print decryptStory()

#
# Build data structures used for entire session and run encryption
#

##if __name__ == '__main__':
    
    # To test findBestShift:
##    wordList = loadWords()
##    s = applyShift('Hello, world!', 8)
##    bestShift = findBestShift(wordList, s)
##    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
##    decryptStory()
