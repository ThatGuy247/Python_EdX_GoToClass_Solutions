# Type your code here
def list_of_primes(n):
    
    def aval(num):
    # prime numbers are greater than 1
        if num > 1:
           # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               lis.append(num)
               return
               
        # if input number is less than
        # or equal to 1, it is not prime
        else:
           return
       
    lis = []
    
    for i in range(2,n):
        aval(i)
        
    return lis
