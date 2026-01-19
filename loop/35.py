number = int(input())
num = abs(number)

sum = 0

if num==0:
    sum = 0
else:
    while num>0:
        digit = num%10
        if digit % 2 == 0:
            sum = sum + digit
        num = num//10
print(sum)
