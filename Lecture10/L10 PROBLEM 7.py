L10 PROBLEM 7
linear search vs. mergeSort + binary search

Application A:

Every time it's asked to, it performs a linear search through list L to find whether it contains x.

Application B:

Sort list L once before doing anything else (using mergeSort).
Whenever it's asked to find x in L, it performs a binary search on L.


What is the worst case time complexity for Application A?
##Application A just performs one linear search through n elements.
##This is O(n) complexity.

What is the worst case time complexity for Application B?
##The time complexity for Application B is how long it takes to do mergeSort once, plus how long it takes to do a binary search.
##That works out to O(nlogn+logn), which is just O(nlogn).

If the application is asked to find x in L k times,
##what is the worst case time complexity for Application A?
##k linear searches so the time complexity is O(kn).

If the application is asked to find x in L k times,
what is the worst case time complexity for Application B?
##Doing the search k times means that the time complexity is how long it takes to do mergeSort once,
##plus how long it takes to do a binary search k times. That works out to O(nlogn+klogn).
##Since we don't know what the value of k is, we cannot simplify further.

What value(s) of k would make Application A be faster
(i.e., asymptotically grow slower than) Application B?
##When k=1, Application A's complexity is O(kn)=O(n),
##and Application B's complexity is O(nlogn+klogn)=O(nlogn+logn).
##Setting k at any value greater than 1 makes O(kn) asymptotically grow faster than O(nlogn+klogn).

What value(s) of k would make Application A grow at the same rate as Application B?
##When k=logn, Application A's complexity is O(kn)=O(nlogn), and Application B's complexity is O(nlogn+klogn)=O(nlogn+lognlogn).
##lognlogn grows slower than nlogn, so in this case Application B's time complexity is O(nlogn).
##So, when k=logn, the order of time complexity of Applications A and B are equal.

Which application should you choose if you know that there are going to be n3 requests to find x in L?
##When k=n3, Application A has time complexity O(n4) whilst Application B's time complexity is O(n3logn).
##Generally we can extrapolate that for very large k, Application B will be the preferred choice.

