def divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        return "divisible by both 3 and 5"
    else:
        return "not divisible by either 3 or 5"
    
num = int(input())
print(divisible(num))
