def alternating_harmonic_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (-1) ** (i + 1) / i
    return total

print(alternating_harmonic_series(5))
