number = int(input())
num = abs(number)

if num == 0:
    smallest = 0
else:
    smallest = num%10
    while num>0:
        digit = num%10
        if digit < smallest:
            smallest = digit
        num = num//10
print(smallest)


# number = int(input())
# num = abs(number)

# smallest = 9

# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num //= 10

# print(smallest)
