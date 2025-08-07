def special_product_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (2 * i - 1) * (2 * i + 1)
    return total

print(special_product_series(5))
