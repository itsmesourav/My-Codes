def nth_term_10(n):
    sequence = [2, 4, 3, 4, 15]
    while len(sequence) < n:
        sequence.append(sequence[-1] + 1)
    return sequence[n - 1]

print(nth_term_10(6))
