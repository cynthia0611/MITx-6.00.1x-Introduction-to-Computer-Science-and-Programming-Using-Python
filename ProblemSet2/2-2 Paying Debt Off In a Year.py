# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/Week_2/Problem_Set_2/
# write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.

# problem set 2-2

def fun(balance, annualInterestRate):    
    fixedPay = balance / 120 * 10
    monthlyInterest = annualInterestRate / 12
    debt = balance # use a initial variable to store start input balue
    # and keep refresh debt value every time
    while debt > 0:
        debt = balance # replace debt value after inner for loop       
        for i in range(1,13): # use two layer loop to control 
            debt -= fixedPay
            if debt <= 0: # set a condition to return fixedPay value
                return fixedPay 
            debt *= (monthlyInterest + 1)
##            print 'month :' + str(i)
##            print 'monthly payment: ' + str(fixedPay)
##            print 'debt :' + str(debt)
##            print '\n'
        fixedPay += 10 #test condition to continue

balance = 5000
annualInterestRate = 0.18

print 'Lowest Payment: '+ str(fun(balance, annualInterestRate))
    





