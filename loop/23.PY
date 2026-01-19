# number = input()

# if number[0] == "-":
#     number = number[1:]
# print(len(number))

number = int(input())

count = 0
number = abs(number)

if number == 0:
    count = 1
else:
    while number>0:
        count = count +1
        number //= 10

print(count)