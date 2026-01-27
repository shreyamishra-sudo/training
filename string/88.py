s = input()
result = ""

for ch in s:
    if 97 <= ord(ch) <= 122:
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)
