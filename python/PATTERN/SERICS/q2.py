def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def summation_fractional_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += i / factorial(i)
    return total

print(summation_fractional_factorials(5))
