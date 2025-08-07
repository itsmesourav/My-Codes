def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def nth_term_15(n):
    return factorial(n) ** 2

print(nth_term_15(5))
