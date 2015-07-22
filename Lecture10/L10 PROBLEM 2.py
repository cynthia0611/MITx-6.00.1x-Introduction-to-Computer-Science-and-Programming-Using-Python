L10 PROBLEM 2  (1/1 point)
In lecture, we saw a version of linear search that used the fact that a set of elements is sorted in increasing order. Here is the code from lecture:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
Consider the following code, which is an alternative version of search.

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False


Return same

##It is equally valid to iterate over the indicies of a list (as in search)
##or iterate over the elements of the list itself (as in search1).
##As we've seen, Python's for statement iterates
##er the items of any sequence (a list or a string),
##in the order that they appear in the sequence. 
