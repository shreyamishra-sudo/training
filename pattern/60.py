n = int(input())

for rows in range(1,n+1):
    for cols in range(rows):
        print(chr(90-cols),end="")
    print()