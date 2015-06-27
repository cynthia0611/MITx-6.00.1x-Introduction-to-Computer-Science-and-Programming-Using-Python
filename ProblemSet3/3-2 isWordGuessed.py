# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/sp13_Problem_Set_3/
# HANGMAN PART 1: IS THE WORD GUESSED
# First, implement the function isWordGuessed that takes in two parameters - 
# a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean 
# - True if secretWord has been guessed 
# (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if lettersGuessed == []:
        return False

    for word in secretWord:
        resultLetterList = []   
        for letter in lettersGuessed:
            result = word ==letter # return True or False for result
            resultLetterList.append(result)
        if True in resultLetterList:
            continue
        else:
            return False
    return True
        
    
##print isWordGuessed('apple',['e', 'i', 'k', 'p', 'r', 's'])
##print isWordGuessed('apple',['a','p','l','e'])
##print isWordGuessed('banana', ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a'])
##print isWordGuessed('grapefruit', [])#False
##print isWordGuessed('durian', ['h', 'a', 'c', 'd',\
##                               'i', 'm', 'n', 'r', 't', 'u'])#True
##print isWordGuessed('grapefruit', [])

