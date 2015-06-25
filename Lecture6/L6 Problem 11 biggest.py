# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_6/
# Returns the key corresponding to the entry with the largest number of values associated with it. 
# If there is more than one such entry, return any one of the matching keys.

animals = {'a': [4, 2, 7, 5, 7, 6], \
'c': [18], 'b': [10, 20, 14, 6, 13, 15, 13, 18, 4, 3],\
'd': [13, 13, 20]}

def biggest(aDict):

    biggestNum = 0
    result = None

    for key in aDict.keys():
        if len(aDict[key]) >= biggestNum:
            result = key
            biggestNum = len(aDict[key]) # variable keep consistance with the value in condition
    return result
print biggest(animals)
