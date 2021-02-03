n = int(input('enter seconds: '))

days = n // 86400
remaining = n % 86400
hours = 0
minutes = 0
second = 0

if remaining != 0:
    hours = remaining // 3600
    remaining %= 3600
else:
    hours = remaining

if remaining != 0:
    minutes = remaining // 60
    remaining %= 60
    
print(str(days) + ' days ' + str(hours) + ' hours ' + str(minutes) +' minutes ' + str(remaining) + ' seconds')
