#Reverse and Double an Integer 

num = int(input("Enter num: "))

rev = 0

if num < 0:
    mul = -1
else:
    mul = 1
num = abs(num)


while num != 0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10

rev = rev * mul

res = rev * 2
print(res)


