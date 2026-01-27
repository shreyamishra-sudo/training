arr1 = list(map(input().split()))
arr2 = list(map(input().split()))

arr3 = []

for n in range(len(arr1)+len(arr2)):
    arr3.append(arr1)
    arr3.append(arr2)
arr3.sort()
print(arr3)
    