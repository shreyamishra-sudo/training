for i in range(1, 1000):
    number = i
    original = i
    total = 0
    count = 0
    
    temp_num = number
    if temp_num == 0:
        count = 1
    else:
        while temp_num > 0:
            count += 1
            temp_num //= 10
            
    temp_num = number
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** count
        temp_num //= 10
        
    if total == original:
        print(original)