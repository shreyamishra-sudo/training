s = input()
count = 0
i = 0

while i < len(s):
    if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
        count += 1
    i += 1

print(count)
