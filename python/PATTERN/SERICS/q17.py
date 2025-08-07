def nth_term_17(n):
    if n % 2 == 0:
        return n * (n + 4)
    else:
        return 0

print(nth_term_17(6))
