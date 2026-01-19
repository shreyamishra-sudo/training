number = int(input())

product = 1
number = abs(number)

if number == 0:
    print(0)
else:
    while number>0:
        product *= number%10
        number//=10
    

    print(product)
    

