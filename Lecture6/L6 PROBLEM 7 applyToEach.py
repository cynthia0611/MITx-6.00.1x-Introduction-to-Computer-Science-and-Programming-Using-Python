# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_6/
# using applyToEach()

testList = [1,-4,8,-9]
##problem 7-a
##  >>> print testList
##  [1, 4, 8, 9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
##print applyToEach(testList,abs)

##problem 7-b
##  >>> print testList
##  [2, -3, 9, -8]

def addOne(s):
        return s + 1

##print applyToEach(testList,addOne)

##problem 7-c
##  >>> print testList
##  [1, 16, 64, 81]
    
def square(s):
    return s**2
print applyToEach(testList,square)
