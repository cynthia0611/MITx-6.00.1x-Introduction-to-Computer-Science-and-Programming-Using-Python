# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_5/

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    
    if exp == 0:
        return 1
    elif exp % 2 ==0:
        return recurPowerNew((base*base),(exp/2))
    else:
        return base * recurPowerNew(base, exp-1)
