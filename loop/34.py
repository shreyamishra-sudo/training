number = int(input())
num = abs(number)

odd_count = 0

if num==0:
    odd_count=0
else:
    while num>0:
        digit = num%10
        if digit % 2 != 0:
            odd_count +=1
        num = num//10
print(odd_count)
