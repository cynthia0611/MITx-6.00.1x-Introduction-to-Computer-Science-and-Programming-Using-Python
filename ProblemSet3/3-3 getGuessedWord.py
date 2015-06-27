# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/sp13_Problem_Set_3/
# This function returns a string that is comprised of letters and underscores, 
# based on what letters in lettersGuessed are in secretWord. 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += '_'
    return ans
    
##secretWord = 'apple' 
##lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a']
##print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's','a'])
##'app_ e'
print getGuessedWord('pineapple', [])
