def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

What is the number of steps it will take to run linearSearch in the worst case?
Express your answer in terms of n, the number of elements in the list L.

2*n + 1

In the worst case scenario, x is not present in L.
Thus we go through the for loop n times.
This means we execute assignment of e to each element of L
(this takes place in the line for e in L) to enter the for loop,
and also execute the check

        if e == x:

once each for every element. So this is 2*n steps.
Finally at the end of the for loop, we execute the return statement one time.
