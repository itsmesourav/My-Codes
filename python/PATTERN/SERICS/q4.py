def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def geometric_series(x, n):
    total = 0
    for i in range(n + 1):
        total += power(x, i)
    return total

print(geometric_series(2, 5))
