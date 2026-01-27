s = input()
count = 0

for ch in s:
    value = ord(ch)
    if (65 <= value <= 90) or (97 <= value <= 122):
        if ch not in 'aeiouAEIOU':
            count += 1

print(count)
