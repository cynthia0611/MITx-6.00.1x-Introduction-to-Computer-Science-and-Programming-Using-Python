# Write an iterative function iterPower(base, exp) 
# that calculates the exponential baseexp by simply using successive multiplication.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here

    result = 1
    while exp>0:
        result = base * result
        exp = exp - 1
    return result



