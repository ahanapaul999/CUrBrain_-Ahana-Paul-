
import math

n = int(input("Enter n: "))
k = int(input("Enter k: "))

factors = []
small = []
large = []

for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        small.append(i)

        if i != n // i:
            large.append(n // i)

factors = small + large[::-1]

if k <= len(factors):
    print("Kth factor =", factors[k - 1])
else:
    print(-1)
