s = input()
count = 0

for ch in s:
    value = ord(ch)
    # if 48 <= ord(ch) <= 57:
    if 48 <= value <= 57:
        count += 1

print(count)
