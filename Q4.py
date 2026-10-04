#Subtract the Product and Sum of Digits


num = int(input("Enter num: "))
sum = 0
mul = 1


num = abs(num)

while num != 0:
    digit = num%10
    sum = sum + digit
    mul = mul * digit
    num = num//10
dif = mul - sum



print(f"dif is == {dif}")