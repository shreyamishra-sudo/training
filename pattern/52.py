n = int(input())

for rows in range(0,n):
    for cols in range(n):
        if rows == 0 or rows == n-1 or cols == 0 or cols == n-1:
            print("*",end =" ")
        else:
            print(" ",end = " ")
    print()
        