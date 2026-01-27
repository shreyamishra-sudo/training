s = input()

found = False

for ch in s:
    count = 0
    for c in s:
        if c == ch:
            count += 1
    if count == 1:
        print(ch)
        found = True
        break

if not found:
    print("no non-repeating character")
