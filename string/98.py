s = input()
rev = ""

# reverse entire string
for i in range(len(s) - 1, -1, -1):
    rev += s[i]

result = ""
word = ""

for ch in rev:
    if ch != ' ':
        word = ch + word
    else:
        result += word + ' '
        word = ""

result += word
print(result)
