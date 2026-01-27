s1 = input()
s2 = input()

len1 = 0
len2 = 0

for _ in s1:
    len1 += 1
for _ in s2:
    len2 += 1

if len1 != len2:
    print("not anagram")
else:
    is_anagram = True
    visited = ""

    for ch in s1:
        if ch not in visited:
            count1 = 0
            count2 = 0

            for c in s1:
                if c == ch:
                    count1 += 1
            for c in s2:
                if c == ch:
                    count2 += 1

            if count1 != count2:
                is_anagram = False
                break

            visited += ch

    if is_anagram:
        print("anagram")
    else:
        print("not anagram")
