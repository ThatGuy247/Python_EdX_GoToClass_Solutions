def remain(principal, annual_interest_rate, duration , number_of_payments):
    n = duration*12
    if annual_interest_rate != 0:  
        r = (annual_interest_rate/100)/12
        remaining = (principal * (((1+r)**n) - ((1+r)**number_of_payments))) / (((1+r)**n)-1)
        return remaining
    else:
        remaining = principal - (principal*(number_of_payments/n))
        return remaining