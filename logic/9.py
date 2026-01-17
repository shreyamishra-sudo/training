def check_range(num1,range1,range2):
    if (range1< num1 <range2) or (range2< num1 <range1):
        return "number in range"
    else:
        return "number not in range"
    
num1,range1,range2 = map(int,input().split())
print(check_range(num1,range1,range2))


# OR THE BELOW CODE USING RANGE FUNCTION

# num, start, end = map(int, input().split())

# if num in range(min(start, end), max(start, end) + 1):
#     print("number in range")
# else:
#     print("number not in range")
