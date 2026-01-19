number = int(input())
num = abs(number)
count = 0

for i in range(1,num+1):
    if num%i == 0:
        count += 1
print(count)

# OPTIMISED

# number = int(input())
# num = abs(number)

# if num == 0:
#     print(0)
# else:
#     count = 0
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             if i == num // i:
#                 count += 1
#             else:
#                 count += 2
#     print(count)
