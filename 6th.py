def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_non_prime(A, B):
    non_primes = []
    for num in range(A, B + 1):
        if not is_prime(num):
            non_primes.append(num)
    return non_primes


A = 12
B = 19
non_prime_numbers = print_non_prime(A, B)
print(", ".join(map(str, non_prime_numbers)))
