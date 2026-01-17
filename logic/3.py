def largest(num1,num2):
    # return max(num1,num2)
    return (num1 + num2 + abs(num1 - num2)) // 2

num1,num2=map(int,input().split())
print(largest(num1,num2))