def check_character(character):
    if len(character)!=1 or not character.isalpha():
        return "invalid input"
    
    if character.isupper():
        return "uppercase"
    else:
        return "lowercase"
    
character = input()
print(check_character(character))

# OR THE BELOW CODE WITHOUT USING THE BUILT-IN FUNCTION

# def check_character(character):
#     if len(character)!=1:
#         return "invalid input"
#     else:
#         value = ord(character)
    
#     if 65<=value<=90:
#         return "uppercase"
#     elif 97<=value<=122:
#         return "lowercase"
#     else:
#         return "invalid input"
    
# character = input()
# print(check_character(character))