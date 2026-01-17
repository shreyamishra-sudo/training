n = int(input())
arr1 = []

for i in range(n):
    arr1.append(int(input()))

for i in range(len(arr1)):
    print(arr1[i], end=" ")
    
arr = list(map(int,input().split()))
for i in range(len(arr)):
    print(arr[i])
    
for value in arr:
    print(value, end=" ")

print()

for i, value in enumerate(arr):
    print(i,value)