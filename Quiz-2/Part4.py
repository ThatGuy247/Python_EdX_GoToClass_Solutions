n = int(input('enter positive number: '))

if n % 2 == 0 and n % 3 ==0:
    print('BOTH')
elif n % 2 ==0 or n % 3 == 0:
    print('ONE')
else:
    print('NEITHER')