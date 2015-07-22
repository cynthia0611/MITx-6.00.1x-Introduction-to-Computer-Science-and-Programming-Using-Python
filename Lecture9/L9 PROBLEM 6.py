L9 PROBLEM 6  (4/4 points)
Consider the following Python procedures.
For each one, specify its order of growth.

# Assume n has been previously bound to some value
i = 0
while i < 5:
   n *= 2
   i += 1

print n 
O(1) - correct

def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result 
O(b) 

def recurPower(a, b):
   print a, b
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1) 
O(b) 

def recurPowerNew(a, b):
   print a, b
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)
O(log(b))
