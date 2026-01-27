s = input()
count = 0

for ch in s:
    if ch in 'aeiou':
        count += 1

print(count)
