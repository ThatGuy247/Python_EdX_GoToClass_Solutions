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