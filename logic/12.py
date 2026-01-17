def last_digit(num):
    last = num%10
    if last == 5:  # if num%10 in (10,5)
        return "last digit is 5"
    elif last == 0:
        return "last digit is 0"
    else:
        return "last digit is not 5 or 0"

num = int(input())
print(last_digit(num)) 