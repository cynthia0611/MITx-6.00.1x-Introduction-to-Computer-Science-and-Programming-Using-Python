def payFun(balance,annualInterestRate,monthlyPaymentRate):
    
    monthlyInterestRate = annualInterestRate/12.0
    totalPay = 0
    
    for i in range(1,2):

        minMonPay = balance * monthlyPaymentRate
        totalPay = minMonPay
        balance = balance - minMonPay
        balance = balance * (1 + monthlyInterestRate)
        
        print 'Month: ' + str(i) 
        print 'Minimum monthly payment: ' +  '%.2f' % minMonPay 
        print 'Remaining balance: ' + '%.2f' % balance

    for i in range(2,13):
        
        minMonPay = balance * monthlyPaymentRate #2
        totalPay += minMonPay
        balance = balance - minMonPay #3
        balance = balance * (1 + monthlyInterestRate)
        
##        balance = balance - balance * monthlyPaymentRate 

        print 'Month: ' + str(i)
        print 'Minimum monthly payment: ' +  '%.2f' % minMonPay 
        print 'Remaining balance: ' + '%.2f' % balance 
    print 'Total paid: ' + '%.2f' % totalPay
    print 'Remaining balance: ' + '%.2f' % balance
    
##print payFun(4213,0.2,0.04)
##print payFun(5000,0.18,0.02)
##print payFun(4842,0.2,0.04)

payFun(balance,annualInterestRate,monthlyPaymentRate)
