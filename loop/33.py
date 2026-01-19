number = int(input())
num = abs(number)

even_count = 0

if num==0:
    even_count=1
else:
    while num>0:
        digit = num%10
        if digit % 2 == 0:
            even_count +=1
        num = num//10
print(even_count)


# STRING BASED SOLUTION

# number = input()

# even_count = 0

# for digit in number:
#     if digit.isdigit() and int(digit) % 2 == 0:
#         even_count += 1

# print(even_count)
