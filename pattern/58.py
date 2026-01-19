n = int(input())

for rows in range(1,n+1):
    for nums in range(1,rows+1):
        print(nums,end="")
            
    for nums in range(rows-1,0,-1):
        print(nums,end="")
    print()