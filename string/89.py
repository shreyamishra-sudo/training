s = input()
result = ""

for ch in s:
    if 65 <= ord(ch) <= 90:
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)
