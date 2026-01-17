n = int(input())
arr = list(map(int, input().split()))
key = int(input())

count = 0
for value in arr:
    if value == key:
        count += 1

print(count)
