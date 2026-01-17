n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
smallest = arr[0]

for i in range(len(arr)):
    if arr[i]<smallest:
        smallest = arr[i]
print(smallest)