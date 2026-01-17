n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
largest = arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest = arr[i]
print(largest)