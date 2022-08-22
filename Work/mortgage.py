# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0
extra_payment = 1000.00
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    current_month += 1
    current_payment = payment
    if ( current_month >= extra_payment_start_month and current_month <= extra_payment_end_month ):
        current_payment += extra_payment    
    principal = principal * (1+rate/12) - current_payment

    #don't pay over remaining balance
    if ( principal < 0):
        current_payment += principal
        principal = 0

    total_paid = total_paid + current_payment
    print(f'%d\t%.2f\t%.2f'%(current_month, total_paid, principal))

print('Total paid {:.2f} over {} months'.format(total_paid, current_month))