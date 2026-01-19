n = int(input())

first = 0
second = 1

if n == 0:
    print(first)
else:
    for _ in range(n):
        next = first + second
        first = second
        second = next 
    print(first)