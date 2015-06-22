# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/Week_2/Problem_Set_2/
# PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

def fun(balance,annualIntrestRate):
    monthlyInterestedRate = annualIntrestRate / 12.0
    lo = balance /12.0
    hi = (balance * (1 + monthlyInterestedRate )**12) / 12.0
    debt = balance
    fixedPay = (lo + hi)/2
##    print fixedPay
    while( lo < (hi-0.001)): # to avoid infinite, define a fixed gap range
        fixedPay = (lo + hi)/2.0
##        print fixedPay
##        print 'lo',lo
##        print 'hi',hi
        debt = balance
        for i in range(12):
            debt = debt - fixedPay
            debt = debt * (1 + monthlyInterestedRate)
        
        if debt <= 0: # pay off
                  
            hi = fixedPay
           
        else: # not pay off this time

            lo = fixedPay 
            
##    if fixedPay%10 == 0:
##        fixedPay = round(fixedPay)
##    else:
##        fixedPay = int(round(fixedPay))/10*10 + 10
       
    print 'Lowest Payment: ' + str('%.2f' %fixedPay)

##fun(5000,0.18)
##fun(320000,0.2) #correct ans shoud be:29157.09
##fun(999999,0.18) #correct ans shoud be:90325.03
fun(balance,annualIntrestRate)
