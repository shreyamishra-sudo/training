s = input("Enter a string: ")

current = ""
longest = ""

for char in s:
    if char in current:
        index = current.find(char)
        current = current[index + 1:]
    current += char
    if len(current) > len(longest):
        longest = current

print("Longest Substring:", longest)