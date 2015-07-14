##PROBLEM 1-1  (1/1 point)
##Suppose x = "pi" and y = "pie". The line of code x, y = y,
##x will swap the values of x and y, resulting in x = "pie" and y = "pi".
##
##True <code>True</code> - correct
##False

##PROBLEM 1-2  (1 point possible)
##Suppose x is an integer in the following code:
##def f(x):
##    while x > 3:
##        f(x+1)
##
##For any value of x, all calls to f are guaranteed to never terminate.
##True
##False <code>True</code> - correct 

##PROBLEM 1-3  (1/1 point)
##A Python program always executes every line of code written at least once.
##True
##False - correct

##PROBLEM 1-4  (1 point possible)
##Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x.
##True
##False - correct

##PROBLEM 1-5  (1 point possible)
##Assume a break statement is executed inside a function. The function call will always terminate without executing any remaining code inside that function.
##True
##False - correct

##PROBLEM 1-6  (1/1 point)
##Let d be a dictionary. If d[a] == d[b] then a == b.
##
##True
##False - correct

##PROBLEM 1-7  (1/1 point)
##Suppose you run the following code:
##def f(L):
##    L.append(4)
##x = [1,2,3]
##f(x)
##
##The variableL is an alias for the variable x.
##True True - correct
##False

##PROBLEM 1-8  (1/1 point)
##A program that keeps running and does not stop is an example of a syntax error.
##
##True
##False - correct

##PROBLEM 1-9  (1/1 point)
##A recursive algorithm must always have at least one base case.
##
##True <span>True </span> - correct
##False

##PROBLEM 1-10  (1/1 point)
##Any number that can be represented as a decimal fraction can be represented exactly in floating point representation in Python.
##
##True
##False - correct

##PROBLEM 2-1  (1/1 point)
##What data type is the object myst:
##
##myst = ( { 1: [1,1], 2: [2,2]}, { 'a': ['a',1], 'b': ['b',2] } )
##tuple tuple - correct
##list
##dictionary
##None of the above

##PROBLEM 2-2  (1/1 point)
##Which of the following is true?
##
##Testing a program and debugging a program are the same thing.
##
##Testing compares program output to the expected output.
##Debugging is a process to study the events leading up to an error. - correct
##
##Testing checks that there is no input on which the program crashes.
##
##Testing is typically done by putting try-except blocks around pieces of code.
##

##PROBLEM 2-3  (1 point possible)
##Assume the statement s[1024] = 3 does not produce an error message. This implies:
##
##type(s) can be str
##type(s) can be tuple
##type(s) can be list
##All of the above - incorrect

##PROBLEM 2-4  (1/1 point)
##Choose the item from the list of potential responses that best matches: "specification"
##
##abstraction abstraction - correct
##mutation
##indentation
##induction

##PROBLEM 2-5  (1/1 point)
##Choose the item from the list of potential responses that best matches: [:]
##
##keyword
##mutation
##cloning cloning - correct
##black box testing

##PROBLEM 3-1  (2 points possible)
##Examine the following code snippet:

##stuff  = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] - correct
##stuff  = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")- correct
##stuff  = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
##stuff  = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
##stuff  = "iPad"
##stuff  = 'iPad'
##for thing in stuff:
##    if thing == 'iPad':
##        print "Found it"

##PROBLEM 3-2  (3 points possible)
##The following Python code is supposed to compute the square of an integer by using successive additions.

##def Square(x):
##    return SquareHelper(abs(x), abs(x))
##
##def SquareHelper(n, x):
##    if n == 0:
##        return 0
##    return SquareHelper(n-1, x) + x
##Not considering recursion depth limitations, what is the wrong with this implementation of procedure Square? Check all that apply.
##
##It is going to return a wrong value.
##The term Square is a reserved Python keyword.
##Function names cannot start with a capital letter.
##The function is never going to return anything.
##Python has arbitrary precision arithmetic.
##This function will not work for negative numbers.
##The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
##Nothing is wrong; the code is fine as-is.

##PROBLEM 4  (10 points possible)
##Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b.
##For example, if x = 16 and b = 2, then the result is 4 - because 24=16.
##If x = 15 and b = 3, then the result is 2 - because 32 is the largest power of 3 less than 15.
##
##In other words, myLog should return the largest power of b such that b to that power
##is still less than or equal to x.
##
##x and b are both positive integers;
##b is an integer greater than or equal to 2.
##Your function should return an integer answer.

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    
    exp = 2
    result = 0
    if x > b:
        while result <= x:
            result = b**exp
            exp += 1
        return exp - 2
    else:
        return 0

print myLog(16,22)

##PROBLEM 5  (10 points possible)
##Write a Python function that returns the sublist of strings in aList
##that contain fewer than 4 characters.
##For example, if aList = ["apple", "cat", "dog", "banana"],
##your function should return: ["cat", "dog"]
##
##This function takes in a list of strings and returns a list of strings.
##Your function should not modify aList.
##
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    bList = []
    for i in range(len(aList)):
        if len(aList[i]) < 4:
            bList.append(aList[i])
    return bList

print lessThan4(["apple", "cat", "dog", "banana"])

##PROBLEM 6  (10 points possible)
##Write a recursive Python function, given a non-negative integer N,
##to calculate and return the sum of its digits.
##
##Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
##while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
##
##This function has to be recursive; you may not use loops!
##
##This function takes in one integer and returns one integer.

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    else:
        return N%10 + sumDigits(N/10)
    
print sumDigits(1234)

##Problem 7 (10/10 points)

##Write a Python function that returns a list of keys in aDict with the value target. 
##The list of keys you return should be sorted in increasing order. 
##The keys and values in aDict are both integers. (If aDict does not contain the value target, 
##you should return an empty list.)

##This function takes in a dictionary and an integer and returns a list.
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    values = aDict.values()
    keysList = []
    if target in values:
        for i in aDict.keys():

            if aDict[i] == target:
                keysList.append(i)

                keysList.sort()

        return keysList
    else:
        return []
print keysWithValue({56:23,2:32,20:34,4:59,5:23,6:23,7:23},23)


##Problem 8 (20/20 points)

##Write a Python function called satisfiesF that has the specification below. 
##Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)

##For your own testing of satisfiesF, for example, the following test function f and test code:

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

Should print:

2
['a', 'a']

##Paste your entire function satisfiesF, including the definition, 
##in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). 
##Do not define f or run_satisfiesF. Do not leave any debugging print statements.
##
##For this question, you will not be able to see the test cases we run. 
##This problem will test your ability to come up with your own test cases.

##Solution 1:
def f(s):
    return 'a' in s

##def satisfiesF(L):
##    """
##    Assumes L is a list of strings
##    Assume function f is already defined for you and it maps a string to a Boolean
##    Mutates L such that it contains all of the strings, s, originally in L such
##            that f(s) returns True, and no other elements
##    Returns the length of L after mutation
##    """
##    # Your function implementation here

    newL = []
    for i in L:

        if f(i) == True:
            newL.append(i)

            #shouldn't modify a list while iterate over it.
    L[:] = newL	

    return len(L)
##
##L = ['a', 'b', 'a','a','c','a','p','w']
L = ['a', 'b', 'a']
##
##print satisfiesF(L)
##print L

##Solution 2:
    
def satisfiesF(L):
    
   rec_list=[]

   for i in range(0,len(L)):
     if(f(L[i])==False):
        rec_list.append(L[i])
        
   for j in rec_list:
       L.remove(j)

   return len(L)
print satisfiesF(L)
##run_satisfiesF(L, satisfiesF)
