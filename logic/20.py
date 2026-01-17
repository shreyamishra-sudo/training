def check_range(num1,range1,range2):
    if (range1<= num1 <=range2) or (range2<= num1 <=range1):
        return "number in range"
    else:
        return "number not in range"
    
num1,range1,range2 = map(int,input().split())
print(check_range(num1,range1,range2))