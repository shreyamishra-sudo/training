def check_age(age):
    if age >= 18:
        return "eligible"
    else:
        return "not eligible"

age = int(input())
print(check_age(age))