##Program 1:

def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

##In the best case scenario, L is an empty list. So we execute only the first assignment statement,
##then the return statement.
##Thus in the best case we execute 2 steps. Note that since the list is empty,
##no assignments are performed in the for x in L line.
##
##In the worst case scenario, L is a long list. In this case we go through the loop for x in L n times.
##Every time through this loop, we execute an assignment of a value to x, and then the inner loop for y in L.
##The assignment takes 1 step on each iteration; how many steps does the inner loop take on each iteration?
##
##The inner loop has three operations (assignment of a value to y, x*y, and list appending).
##So the inner loop executes 3*n times on each iteration of the outer loop.
##Thus the nested loop structure is executed n * (3*n + 1) = 3*n**2 + n times!
##
##Adding in two steps (for the first assignment statement,
##and the return statement) we see that in the worst case,
##this program executes 3*n**2 + n + 2 steps.


##Program 2:

def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares

##In the best case scenario, L is an empty list. So we execute only the first assignment statement, then the return statement.
##Thus in the best case we execute 2 steps. Note that since the list is empty, no assignments are performed in the for x in L line.
##
##In the worst case scenario, L is a long list of one repeated number (ie [2, 2, 2, 2, ...].
##In this case we go through the loop for x in L n times.
##Every time through this loop, we perform one assigment of a value to the variable x,
##then we execute the inner loop for y in L n times.
##
##The inner loop performs one assigment of a value to the variable y.
##It then has one operation that is checked every time (if x == y).
##Since the WORST case is when the list is composed of identical elements,
##this check is always true - so the third and fourth operations (x*y, and list appending) are always performed.
##So the inner loop executes 4*n times on each iteration of the outer loop.
##Thus the nested loop structure is executed n * (4*n + 1) = 4*n**2 + n times!
##
##Adding in two steps (for the first assignment statement,
##and the return statement) we see that in the worst case, this program executes 4*n**2 + n + 2 steps.


##Program 3:

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection
##In the best case scenario, L1 is an empty list.
##So we execute only the first assignment statement, then the return statement.
##Thus in the best case we execute 2 steps.
##
##In the worst case scenario, every element of L1 is the same as the very last element of L2.
##In this case we go through the loop for elt in L1 n times. Every time through this loop,
##we perform one assigment of a value to the variable elt, then	we execute the check if elt in L2.
##
##How long does it take to execute this check? Well in the worst case,
##elt is the very LAST element of L2. In order to check if elt in L2,
##Python iterates over the elements of L2 until it either finds the one you're looking for, or L2 runs out of elements. Thus in the worst case, the check if elt in L2 takes n steps. After this, we perform one append operation. So the conditional plus the append takes n + 1 steps on each iteration of the loop. Thus the for loop takes n * (n + 2) = n**2 + 2*n steps!
##
##Adding in two steps (for the first assignment statement,
##and the return statement) we see that in the worst case, this program executes n**2 + 2*n + 2 steps.






