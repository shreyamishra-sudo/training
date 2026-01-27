s = input()
rev = ""

i = 0
length = 0
for _ in s:
    length += 1

while length > 0:
    rev += s[length - 1]
    length -= 1

print(rev)
