def nth_fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b        
n = 8
fib_sequence = [nth_fibonacci(i) for i in range(1, n + 1)]
print(" ".join(map(str, fib_sequence)))
