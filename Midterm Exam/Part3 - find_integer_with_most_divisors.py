def find_integer_with_most_divisors(input_list):
    holder = []
    hold = 0
    for item in input_list:
        c=0
        for i in range(1,item+1):
            if item % i ==0:
                c += 1
        holder.append(c)
    maximum = max(holder)
    for i in range(len(holder)):
        if holder[i] == maximum:
            return input_list[i]