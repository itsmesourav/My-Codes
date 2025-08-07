def triple_product_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i * (i + 1) * (i + 2)
    return total

print(triple_product_series(5))
