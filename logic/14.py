def multiple_check(num1,num2):
    if num1 == 0 and num2 == 0:
        return "not a multiple"
    if num1 == 0 or num2 == 0:
        return "multiple"
    
    if (num1 % num2 == 0) or (num2 % num1 == 0):
        return "multiple"
    else:
        return "not a multiple"

num1,num2 = map(int,input().split())
print(multiple_check(num1,num2))