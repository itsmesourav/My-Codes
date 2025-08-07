def nth_term_12(n):
    if n % 2 == 0:
        return (n // 2) - 1
    else:
        return 2 * (n // 2)

print(nth_term_12(6))
