# L5 PROBLEM 6  
# Although Python provides a built-in function for computing the length of a string, we can write our own.

# Write an iterative function, lenIter, 
# which computes the length of an input argument (a string), 
# by counting up the number of characters in the string.

def lenIter(aStr):
    count = 0
    for i in aStr:
        count += 1
    return count
print lenIter('a !! ')
