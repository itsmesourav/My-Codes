def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def summation_fractional_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i / power(i, i)
    return total

print(summation_fractional_powers(5))
