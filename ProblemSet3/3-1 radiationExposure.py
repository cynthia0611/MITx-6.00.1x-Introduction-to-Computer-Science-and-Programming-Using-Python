# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/sp13_Problem_Set_3/
def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''

    sumTotal = 0

    point = start
    while point >= start and point < stop:
        sumSub = step * f(point)
        sumTotal += sumSub
        point += step
    return sumTotal

print radiationExposure(0, 4, 0.25)
print radiationExposure(5, 10, 0.25)
print radiationExposure(0, 3, 0.1)
print radiationExposure(100, 400, 4)
print radiationExposure(600, 1200, 5)
print radiationExposure(0, 40, 1)

