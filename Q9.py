def next_prime(n):
    if n < 2:
        return 2
    
    candidate = n + 1
    while True:
        is_prime = True
        i = 2
        while i * i <= candidate:
            if candidate % i == 0:
                is_prime = False
                break
            i += 1
            
        if is_prime:
            return candidate
        candidate += 1

if __name__ == "__main__":
    n = 10
    print(next_prime(n))