def string_check(str1,str2):
    if len(str1) != len(str2): 
        return "strings are not equal"
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return "strings are not equal"
    return "srtings are equal"

str1 = input()
str2 = input()
print(string_check(str1,str2))


# def string_check(str1,str2):
#     if str1 == str2: 
#         return "strings are equal"
#     else:
#         return "strings are not equal"
    
# str1 = input()
# str2 = input()
# print(string_check(str1,str2))

