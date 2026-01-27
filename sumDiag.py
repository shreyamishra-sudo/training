n = int(input("Enter the size of the square matrix (n): "))

matrix = []
left = 0
right = 0

print(f"Enter the {n*n} elements row by row (space-separated):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
for i in range(n):
    right += matrix[i][i]
    left += matrix[i][n-1-i]

print(left,right)