def check_character(char):
    if len(char) != 1:
        return "invalid input"
    
    value = ord(char)
    
    if 65<=value<=90 or 97<=value<=122: # if char.isalpha()
        return "character"
    elif 48<=value<=57: # if char.isdigit
        return "digit"
    else:
        return "special character"
    
char = input()
print(check_character(char)) 

