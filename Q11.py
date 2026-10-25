def modular_addition(arr):
    MOD = 10**9 + 7
    total_sum = 0
    for num in arr:
        total_sum = (total_sum + num) % MOD
    return total_sum