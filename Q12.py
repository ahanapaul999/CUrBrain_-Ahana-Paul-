def modulo_power(base, power, MOD):
    result = 1 % MOD
    for _ in range(power):
        result = (result * base) % MOD
    return result