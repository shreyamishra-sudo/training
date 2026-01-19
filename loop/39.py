import math

num = int(input())
is_Prime = True

if num <= 1:
    is_Prime = False
else:
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            is_Prime = False
            
if is_Prime == True:
    print("prime")
else:
    print("not prime")