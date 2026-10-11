def count_primes(n):
    if n <= 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while p * p < n:
        if is_prime[p]:
            multiple = p * p
            while multiple < n:
                is_prime[multiple] = False
                multiple += p
        p += 1
        
    count = 0
    for i in range(n):
        if is_prime[i]:
            count += 1
            
    return count

if __name__ == "__main__":
    n = 10
    print(count_primes(n))