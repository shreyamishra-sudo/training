n = int(input("Enter size of n x n matrix: "))
matrix = []

print(f"Enter {n} rows (space-separated):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
above_sum = 0
below_sum = 0

for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            above_sum += matrix[i][j]
        elif i + j > n - 1:
            below_sum += matrix[i][j]

print(f"Sum above the diagonal: {above_sum}")
print(f"Sum below the diagonal: {below_sum}")