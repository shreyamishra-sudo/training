number = int(input())

num = abs(number)
original = number
reverse = 0

while num>0:
    reverse = reverse*10 + num%10
    num = num//10

if number<0:
    reverse = -reverse

if original == reverse:
    print("palindrome")
else:
    print("not a palindrome")