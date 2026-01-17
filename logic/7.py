def check_character(character):
    character = character.lower()
    if len(character)!=1 or not character.isalpha():
        return "invalid input"
    
    #if character in "aeiou" --> this can also be used
    
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        return "vowel"
    else:
        return "consonant"
    
character = input()
print(check_character(character))