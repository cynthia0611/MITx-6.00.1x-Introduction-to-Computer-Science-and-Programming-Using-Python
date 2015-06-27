# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/sp13_Problem_Set_3/
# This function returns a string that is comprised of letters and underscores, 
# based on what letters in lettersGuessed are in secretWord. 

# solution 1
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
    
# solution 2    
def getGuessedWord(secretWord, lettersGuessed):   

    newList = []   
    for word in secretWord:
        flag = False # refresh every time when finish inner loop
                     # use flag to control when to output '_'
        for letter in lettersGuessed:
            if word == letter:
                flag = True
                newList.append(word)
                break # finish this inner loop
                      # avoid to compare the rest letters
        if(flag == False):
            newList.append('_')   
   
    return newList
##secretWord = 'apple' 
##lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a']
##print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's','a'])
##'app_ e'
print getGuessedWord('pineapple', [])
