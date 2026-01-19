num = int(input())
fact = 1
if num<0:
    print("factorial undifined")
elif num == 0 or num == 1:
    print(fact)
else:
    for i in range (2,num+1):
        fact = fact * i
    print(fact)