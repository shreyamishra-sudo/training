n = int(input())
arr = list(map(int, input().split()))
key = int(input())

index = -1

for i in range(n):
    if arr[i] == key:
        index = i
        break

print(index)
