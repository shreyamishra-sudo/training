def last_digit(num1,num2):
    last1 = num1%10
    last2 = num2%10
    if last1 == last2:
        return "same last digit"
    else:
        return "last digits are not same"

num1,num2 = map(int,input().split())
print(last_digit(num1,num2)) 


# ALTERNATIVE SHORTER CODE

# def last_digit(a, b):
#     return "same last digit" if a % 10 == b % 10 else "last digits are not same"
