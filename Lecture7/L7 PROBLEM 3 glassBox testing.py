def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger
    
# Test Suite A: 
# maxOfThree(2, -10, 100), maxOfThree(7, 9, 10), maxOfThree(6, 1, 5), maxOfThree(0, 40, 20) 
