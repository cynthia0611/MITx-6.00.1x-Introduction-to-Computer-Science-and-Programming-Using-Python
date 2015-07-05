def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """

Test cases:   
 set1 is an empty set; 
 set2 is an empty set  set1 is an empty set; 
 set2 is of size greater than or equal to 1  set1 is of size greater than or equal to 1; 
 set2 is an empty set  set1 and set2 are both nonempty sets which do not contain any objects in common  
 set1 and set2 are both nonempty sets which contain objects in common
