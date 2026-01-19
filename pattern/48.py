n = int(input())

# for rows in range(5,0,-1):
#     for cols in range(rows):
#         print("*",end ="")
#     print()
    
for rows in range(1,n+1):
    for cols in range(n-rows+1):
        print("*",end ="")
    print()
        