L10 PROBLEM 3  (1/1 point)
In lecture, we saw a version of linear search that used the fact that a set of elements is sorted in increasing order. Here is the code from lecture:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
Consider the following code, which is an alternative version of search.

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False
Return the same

##The change from an if statement, in line 5 of search1, to an elif statement,
##in line 5 of search2, does not change the behavior of the function.
