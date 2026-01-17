n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))
    
positive_count=0
negative_count=0
zero_count=0

for i in range(len(arr)):
    if arr[i]>0:
        positive_count+=1
    elif arr[i]<0:
        negative_count+=1
    else:
        zero_count+=1
        
print(positive_count)
print(negative_count)
print(zero_count)