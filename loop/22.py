n = int(input("enter the number of times for looping: "))

for i in range(1,n+1): # OR for i in range(6,n+1,6): print(i)
    if i % 3 == 0 and i % 2 ==0:
        print(i)
 