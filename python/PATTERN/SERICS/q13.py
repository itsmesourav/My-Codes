def nth_term_13(n):
    if n % 2 == 1:
        return 14 * ((n // 2) + 1)
    else:
        return 20 * (n // 2)

print(nth_term_13(6))
