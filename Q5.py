#Replace Even Digits with Zero 

n = int(input("Enter number: "))

result = []

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        result.append(0)
    else:
        result.append(digit)
    n = n // 10

result.reverse()

print(result)