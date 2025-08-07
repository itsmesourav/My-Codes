def custom_linear_series(n):
    sequence = [1, 2]
    for i in range(3, n + 1):
        sequence.append(11 * i - 11)
    return sequence

print(custom_linear_series(5))
