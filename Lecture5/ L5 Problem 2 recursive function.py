##L5 Problem 2
##Write a function recurPower(base, exp) which computes baseexp by recursively calling itself
##to solve a smaller version of the same problem,
##and then multiplying the result by base to solve the initial problem.

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 0:
        return 1
    return base * recurPower(base,(exp-1))
