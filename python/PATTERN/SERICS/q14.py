def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def nth_term_14(n):
    return factorial(n - 1)

print(nth_term_14(5))
