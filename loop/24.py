number = int(input())

total = 0
number = abs(number)

while number>0:
    total += number%10
    number//=10
    

print(total)