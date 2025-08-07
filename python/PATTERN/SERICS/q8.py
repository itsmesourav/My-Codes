def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def even_exponential_series(x, n):
    total = 0
    for i in range(0, 2 * n + 1, 2):
        total += (-1) ** (i // 2) * power(x, i) / factorial(i)
    return total

print(even_exponential_series(2, 5))
