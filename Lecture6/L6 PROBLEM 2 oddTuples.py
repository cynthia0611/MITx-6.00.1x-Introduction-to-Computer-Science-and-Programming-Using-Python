# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_6/
# oddTuples, which takes a tuple as input, and returns a new tuple as output, 
# where every other element of the input tuple is copied, starting with the first one. 
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    newTu = ()
    for i in range(0, len(aTup)):
        if i % 2 == 0:
            newTu += (aTup[i],) # make it possible to add a new element to the end of the tuple
            # tupel is not mutable
            # singleton of tuple is tuple(x,), pay attention of the comma 
    return newTu

##print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
print oddTuples(())
print oddTuples((20, 19, 4, 7, 19, 5, 12, 9))
print oddTuples((8, 3, 17, 3, 9, 1))
print oddTuples((18, 0, 3, 9, 12, 14, 10, 13))
