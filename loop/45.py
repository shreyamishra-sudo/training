number = int(input())
total = 0
count = 0
number = abs(number)
original = number

if number == 0:
    count = 1
else:
    while number>0:
        count = count +1
        number //= 10
        
number = original
while number>0:
    digit = number%10
    total = total+digit**count
    number//=10
if (total == original):
    print("armstrong")
else:
    print("not armstrong")