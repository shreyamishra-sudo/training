s = input()
is_alpha = True

for ch in s:
    if not ((65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122)):
        is_alpha = False
        break

if is_alpha:
    print("only alphabets")
else:
    print("not only alphabets")
