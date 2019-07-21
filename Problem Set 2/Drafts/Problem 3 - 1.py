# Paste your code into this box
n = 0

x = balance

payment = x/12

minPayment = x/12
maxPayment = (x * (1 + (annualInterestRate/12.0)**12)/12.0)

while True:
    x = balance
    for months in range(0, 12):
        monthlyUnpaidBalance = x - payment
        x = round(monthlyUnpaidBalance + ((annualInterestRate/12.0) * monthlyUnpaidBalance), 2)
    if x <= 0:
        break
    else:
        if payment <= (minPayment + maxPayment)/2:
            maxPayment = (minPayment + maxPayment)/2
            payment += 0.01
            n += 1
        else:
            minPayment = (minPayment + maxPayment)/2
            payment += 0.01
            n += 1
        
payment = round(payment, 2)
                          
print("Lowest Payment: " + str(payment))
