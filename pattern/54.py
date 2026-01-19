n = int(input())

for rows in range(1,n+1):
    for space in range(rows-1):
        print(" ",end="")
    for stars in range(2*(n-rows)+1):
            print("*", end="")
    print()