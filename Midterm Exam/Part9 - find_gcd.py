def find_gcd(lis):
    def find(x, y): 

        while(y): 
            x, y = y, x % y 

        return x 

    num1 = lis[0] 
    num2 = lis[1] 
    gcd = find(num1, num2) 
      
    for i in range(2, len(lis)): 
        gcd = find(gcd, lis[i]) 

    return gcd