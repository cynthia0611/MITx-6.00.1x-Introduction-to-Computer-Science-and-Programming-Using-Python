# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_5/
# use the idea of bisection search to determine if a character is in a string, 
# so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're looking for (the "test character"). 
# If they are the same, we are done - we've found the character we're looking for!

# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''

# Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])
