# mortgage.py
#
# Exercise 1.7

#Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.


#Exercise 1.8: Extra payments
#Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    month = month + 1 
    principal = principal * ( 1 + rate/12) - payment
    total_paid = total_paid + payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(month, round(total_paid,2), round(principal,2))
print('Total paid',round(total_paid,1))
print('Total months:', month)
