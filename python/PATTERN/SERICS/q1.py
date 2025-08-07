def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def summation_factorials(n):
    total = 11
    for i in range(2, n + 1):
        total += factorial(i)
    return total

print(summation_factorials(5))
