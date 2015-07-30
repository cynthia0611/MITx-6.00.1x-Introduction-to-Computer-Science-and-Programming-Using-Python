1. Thinking about the genPrimes generator from the last problem,
which of the following can be done only by using a generator,
instead of defining a function
(that uses any type of construct we've learned about, except generators)?

def genPrimesFn():
    '''Function to return 1000000 prime numbers'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 1000000:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes

def genPrimesFn():
    '''Function to print every 10th prime 
    number, until you've printed 20 of them.'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    counter = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0:
                # Print every 10th prime
                print last
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
                return



def genPrimesFn():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
            else:
                primes.append(last)
                print last
                uinp = raw_input("Print the next prime? [y/n] ")
                while uinp != 'y' and uinp != 'n':
                    while uinp
                    print "Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no."
                    uinp = raw_input("Print the next prime? [y/n] ")
                if uinp == 'n':
                    break


2. Every procedure that has a yield statement is a generator.
See http://docs.python.org/release/2.3.5/ref/yield.html.
The Python documentation is always your friend!

4.Suppose we wanted to iterate over a million numbers using a 'for/in' loop.
If we use the code for x in range(1000000),
how many numbers do we need to store in memory at once?
 
We need to store 1000000 numbers. This for loop first makes a list of 1000000 integers,
then iterates over that list.
So the entire list of 1000000 numbers must be saved in memory until the iteration has completed.

5. If we were to use a generator to iterate over a million numbers,
how many numbers do we need to store in memory at once?

We need to store 2 numbers - one for the current value, and one for the max value.
def genOneMillion():
    maxNum = 1000000
    current = -1
    while current < maxNum:
        current += 1
        yield current
Python actually provides this! The xrange function,
while not really a generator, has the same benefits of using a generator.
You can substitue xrange any place in your code that uses range. It behaves the same way,
but stores much less information in memory so can cause your code to execute somewhat faster.









