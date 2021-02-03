def remain(principal, annual_interest_rate, duration , number_of_payments):
    def vam(principal:float, annual_interest_rate:float, duration:int):
        if annual_interest_rate != 0:
            n = duration*12
            r = (annual_interest_rate/100)/12
            x = (r+1)**n
            y = (principal*r*x)
            month_pay = y / (((1+r)**n) - 1)
            return month_pay
        else:
            n = duration*12
            month_pay = principal/n
            return month_pay

    n = duration*12
    if annual_interest_rate != 0:  
        r = (annual_interest_rate/100)/12
        remaining = (principal * (((1+r)**n) - ((1+r)**number_of_payments))) / (((1+r)**n)-1)
        pay = vam(principal, annual_interest_rate, duration)
        return pay, remaining
    else:
        remaining = principal - (principal*(number_of_payments/n))
        pay = vam(principal, annual_interest_rate, duration)
        return pay, remaining

principal = float(input('Enter loan amount: '))
annual_interest_rate = float(input('Enter annual interest rate (percent): '))
duration = int(input('Enter loan duration in years: '))

pay, ok = remain(principal, annual_interest_rate, duration, 0)

print(f'LOAN AMOUNT: {int(principal)} INTEREST RATE (PERCENT): {int(annual_interest_rate)}')
print(f'DURATION (YEARS): {int(duration)} MONTHLY PAYMENT: {int(pay)}')

for i in range(duration):
    pay, ok = remain(principal, annual_interest_rate, duration, (i+1)*12)
    print(f'YEAR: {i+1} BALANCE: {int(ok)} TOTAL PAYMENT {int((i+1)*12*pay)}')
