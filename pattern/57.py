n = int(input())

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        if (rows+cols)%2 == 0:
            print("1",end="")
        else:
            print("0",end="")
    print()
        