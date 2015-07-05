def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      #return n
      return 1
   else:
      return n * f(n-1)
      
      
##This is a function known as factorial
##- the product of all the numbers from 1 through n.
##The base case of factorial is 0! = 1,
##but the original code was written with the base case 0! = 0.
##You can see why the original code was broken by writing out
##the recursive expansion of f(3):
##
##f(3)=3∗f(2)
##3∗(2∗f(1))
##3∗(2∗(1∗f(0)))
##3∗(2∗(1∗(0)))
##3∗(2∗(0))
##3∗(0)
##0
##The fixed version of the code puts the line return 1,
##instead of return n, when n == 0.
##We can see that this modified version of the code fixes
##the factorial function by again writing out
##the recursive expansion of f(3):
##
##f(3)=3∗f(2)
##3∗(2∗f(1))
##3∗(2∗(1∗f(0)))
##3∗(2∗(1∗(1)))
##3∗(2∗(1))
##3∗(2)
##6
