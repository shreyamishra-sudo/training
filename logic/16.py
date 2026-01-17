def check_num(num):
    if (num % 4 == 0) and (num % 8 !=0):
        return "divisible by 4 but not by 8"
    else:
        return "divisible by other numbers"

num = int(input())
print(check_num(num))