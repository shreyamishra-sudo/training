# arr = list(map(int,input().split()))
# total = 0

# for value in arr:
#     total+=value
# print(total)

n = int(input())
arr1 = []
total = 0

for i in range(n):
    arr1.append(int(input()))

for i in range(len(arr1)):
    total+=arr1[i]
    
print(total)