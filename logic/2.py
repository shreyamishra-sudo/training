def classify(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
        
num = float(input())
print(classify(num))