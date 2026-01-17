def triangle(side1,side2,side3):
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        return "triangle possible"
    else:
        return "triangle not possible"
    
side1,side2,side3 = map(int,input().split())
print(triangle(side1,side2,side3))