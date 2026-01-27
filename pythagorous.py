a = list(map(int,input().split()))

n = len(a)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if (a[i]**2 + a[j]**2 == a[k]**2) or (a[i]**2 + a[k]**2 == a[j]**2) or (a[j]**2 + a[k]**2 == a[i]**2):
                print(a[i],a[j],a[k])
            else:
                print("none")
                
                    
                