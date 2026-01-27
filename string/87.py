s = input()
rev = ""

length = 0
for _ in s:
    length += 1

temp = length
while temp > 0:
    rev += s[temp - 1]
    temp -= 1

if s == rev:
    print("palindrome")
else:
    print("not palindrome")
