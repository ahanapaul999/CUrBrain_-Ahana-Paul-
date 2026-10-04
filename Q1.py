
#Count Digits Without String Conversion

num = int(input("Enter num: "))


if num == 0:
    count=1
else:
    count=0

    num = abs(num)    
    while num!=0:
        count+=1
        num = num//10

if count % 2 == 0:
    print(True)
else:
    print(False)            