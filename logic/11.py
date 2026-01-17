def triangle(side1,side2,side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "triangle not possible"
    
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        if side1 == side2 and side2 == side3 and side3 == side1:
            return "equilateral triangle"
        elif side1 != side2 and side2 != side3 and side3 != side1:
            return "scalene triangle"
        else:
            return "isosceles triangle"
    else:
        return "triangle not possible"
    
side1,side2,side3 = map(int,input().split())
print(triangle(side1,side2,side3))