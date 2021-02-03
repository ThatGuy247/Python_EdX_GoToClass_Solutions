n = int(input('enter working time hours: '))

if n < 0 or n > 168:
    print('INVALID')
    
elif n <= 40:
    pay = int(n*8)
    print('YOU MADE ' + str(pay) + ' DOLLARS THIS WEEK')
    
elif n <= 50:
    minus = n - 40
    pay = int((40*8) + minus*9)
    print('YOU MADE ' +str(pay) + ' DOLLARS THIS WEEK')
    
else:
    minus = n - 50
    pay = int((40*8) + (10*9) + minus*10)
    print('YOU MADE ' + str(pay) + ' DOLLARS THIS WEEK')
