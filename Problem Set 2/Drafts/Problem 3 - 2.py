#for months in range(0, 12):
#    monthlyUnpaidBalance = x - payment
#    x = round(monthlyUnpaidBalance + ((annualInterestRate/12.0) * monthlyUnpaidBalance), 2)
#    
#
#lowestPayment = 10
#
#while True:
#    x = balance
#    for months in range(0, 12):
#        monthlyUnpaidBalance = x - lowestPayment
#        x = round(monthlyUnpaidBalance + ((annualInterestRate/12.0) * monthlyUnpaidBalance), 2)
#    if x <= 0:
#        break
#    else:
#        lowestPayment += 10
#               
#print("Lowest Payment: " + str(lowestPayment))


#def f(balance, annualInterestRate):
#    count = 0
#    a = x = y = balance
#    monthlyInterestRate = annualInterestRate / 12.0
#    lowerBound = balance / 12
#    upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
#    payment = ((lowerBound + upperBound) / 2) + 1    
#    for months in range(0, 12):
#        min_monthlyUnpaidBalance = x - upperBound
#        min_x = min_monthlyUnpaidBalance + (monthlyInterestRate * min_monthlyUnpaidBalance)
#        x = min_x
#        max_monthlyUnpaidBalance = y - lowerBound
#        max_x = max_monthlyUnpaidBalance + (monthlyInterestRate * max_monthlyUnpaidBalance)
#        y = max_x
#    while True: 
#        a = balance
#        for months in range(0, 12):
#            monthlyUnpaidBalance = a - payment
#            a = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)            
#        if a < 0 and abs(a) >= 0.1:
#            upperBound = (lowerBound + upperBound) / 2
#            payment = (lowerBound + upperBound) / 2 
#            count += 1
#        elif a > 0 and abs(a) >= 0.1:
#            lowerBound = (lowerBound + upperBound) / 2
#            payment = (lowerBound + upperBound) / 2 
#            count += 1
#        else:
#            break
#    return print("Lowest Payment: " + str(round(payment, 2)))
#
#f(320000, 0.2)


import time
start = time.time()
"the code you want to test stays here"

balance = 320000
annualInterestRate = 0.2


count = 0
a = x = y = balance
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
payment = ((lowerBound + upperBound) / 2) + 1    
for months in range(0, 12):
    min_monthlyUnpaidBalance = x - upperBound
    min_x = min_monthlyUnpaidBalance + (monthlyInterestRate * min_monthlyUnpaidBalance)
    x = min_x
    max_monthlyUnpaidBalance = y - lowerBound
    max_x = max_monthlyUnpaidBalance + (monthlyInterestRate * max_monthlyUnpaidBalance)
    y = max_x
while True: 
    a = balance
    for months in range(0, 12):
        monthlyUnpaidBalance = a - payment
        a = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)            
    if a < 0 and abs(a) >= 0.1:
        upperBound = (lowerBound + upperBound) / 2
        payment = (lowerBound + upperBound) / 2 
        count += 1
    elif a > 0 and abs(a) >= 0.1:
        lowerBound = (lowerBound + upperBound) / 2
        payment = (lowerBound + upperBound) / 2 
        count += 1
    else:
        break

print("Lowest Payment: " + str(round(payment, 2)))
        
end = time.time()
print(end - start)
            
            
