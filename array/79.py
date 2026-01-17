n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

merged = []

for value in arr1:
    merged.append(value)
for value in arr2:
    merged.append(value)

print(merged)
