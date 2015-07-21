Program 1:

def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

In the best case scenario, L is an empty list. So we execute only the first assignment statement, then the return statement.
Thus in the best case we execute 2 steps. Note that since the list is empty, no assignments are performed in the for x in L line.

In the worst case scenario, L is a long list of one repeated number (ie [2, 2, 2, 2, ...].
In this case we go through the loop for x in L n times.
Every time through this loop, we perform one assigment of a value to the variable x,
then we execute the inner loop for y in L n times.

The inner loop performs one assigment of a value to the variable y.
It then has one operation that is checked every time (if x == y).
Since the WORST case is when the list is composed of identical elements,
this check is always true - so the third and fourth operations (x*y, and list appending) are always performed.
So the inner loop executes 4*n times on each iteration of the outer loop.
Thus the nested loop structure is executed n * (4*n + 1) = 4*n**2 + n times!

Adding in two steps (for the first assignment statement,
and the return statement) we see that in the worst case, this program executes 4*n**2 + n + 2 steps.



