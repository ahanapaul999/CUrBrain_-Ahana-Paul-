#Palindrome or Sum with Reverse

num = int(input("Enter num: "))

temp = num
rev = 0

if num < 0:
    mul = -1
else:
    mul = 1

num = abs(num)

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

rev = rev * mul

if temp == rev and temp >= 0:
    print(temp)

else:
    res = temp + rev
    print(res)