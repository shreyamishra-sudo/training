s = input()
is_digit = True

for ch in s:
    if not (48 <= ord(ch) <= 57):
        is_digit = False
        break

if is_digit:
    print("only digits")
else:
    print("not only digits")
