def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count
   
# Test Suite B: foo(10, 3), foo(1, 4), foo(10, 6)
