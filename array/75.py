n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(1, n, 2):
    total += arr[i]

print(total)
