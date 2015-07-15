L9 Problem 2(6 points possible)
Problem 2-1
For the following programs, fill in the best-case and the worst-case number of steps
it will take to run each program.

For these questions, you'll be asked to write a mathematical expression.
Use +, -, / signs to indicate addition, subtraction,
and division. Explicitly indicate multiplication
with a * (ie say "6*n" rather than "6n"). Indicate exponentiation with a caret (^)
(ie "n^4" for n4). Indicate base-2 logarithms with the word log2 followed by parenthesis (ie "log2(n)").

    Program 1:

    def program1(x): # in the best case, x = 0 
        total = 0
        for i in range(1000): # 3000 for the for loop whatever x is 
            total += i 

        while x > 0: # 5 steps in while loop
            x -= 1  # -= is 2 steps, and also += is 2 steps
            total += x

        return total

What is the number of steps it will take to run Program 1 in the best case?
Express your answer in terms of n, the size of the input x.

3003

The for loop is 1 and the += is 2. One step to do the addition, one for the =.


What is the number of steps it will take to run Program 1 in the worst case?
Express your answer in terms of n, the size of the input x.

In the best case scenario, x is less than or equal to 0.
We first execute the assignment total = 0 for one step. Next we execute the for i in range(1000) loop.
This loop is executed 1000 times and has three steps
(one for the assignment of i each time through the loop, as well as two for the += operation)
on each iteration. We next check if x > 0 - it is not so we do not enter the loop.
Adding one more step for the return statement,
in the best case we execute 1 + 3*1000 + 1 + 1 = 3003 steps.

In the worst case scenario,
x is a large positive number.
In this case, we first execute the assignment total = 0 for one step.
Next we execute the first loop 1000 times (3000 total steps),
then we execute the second loop (while x > 0) n times.
This loop has five steps (one for the conditional check, x > 0, and two each for the -= and += operations).
When we finally get to the point where x = 0,
we execute the conditional check x > 0 one last time - since it is not,
we do not enter the loop. Adding one more step for the return statement,
in the worst case we execute 1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003 steps.

Problem 2-1
Program 2:

def program2(x):
    total = 0 # 1
    for i in range(1000): # 2000 for this for loop
        total = i

    while x > 0: # 1*log2(n)
        x /= 2 # 2*log2(n)
        total += x # 2*log2(n)

    return total # 

What is the number of steps it will take to run Program 2 in the best/worse case?
Express your answer in terms of n, the size of the input x.
