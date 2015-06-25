# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_6/
# returns the sum of the number of values associated with a dictionary.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
##print animals

def howManyValue(aDict):
    result = 0
    for value in aDict.values():
        result += len(value)
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
    return result
print howManyValue(animals)


def howManyKey(aDict):
    result = 0
    for key in aDict:
        result += len(aDict[key])
    return result
print howManyKey(animals)
