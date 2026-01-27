s = input()
key = input()   
count = 0

for ch in s:
    if ch == key:
        count += 1

print(count)
