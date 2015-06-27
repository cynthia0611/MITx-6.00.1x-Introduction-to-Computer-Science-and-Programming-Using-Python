# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/sp13_Problem_Set_3/
# returns a string that is comprised of lowercase English letters - 
# all lowercase English letters that are not in lettersGuessed.
#  using string.ascii_lowercase, which is a string comprised of all lowercase letters:
# >>> import string
# >>> print string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    letterList = list(string.ascii_lowercase)
    outString = ''
    for letter in lettersGuessed:
        letterList.remove(letter)
    for char in letterList:
        outString += char
    return outString

##print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) # abcdfghjlmnoqtuvwxyz
