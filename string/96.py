s = input()
visited = ""
found = False

for ch in s:
    if ch in visited:
        print(ch)
        found = True
        break
    else:
        visited += ch

if not found:
    print("no repeating character")
