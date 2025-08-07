def nth_term_11(n):
    sequence = [3, 5, 33, 35, 53]
    while len(sequence) < n:
        sequence.append(sequence[-1] + 20)
    return sequence[n - 1]

print(nth_term_11(6))
