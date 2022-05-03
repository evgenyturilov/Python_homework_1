# Определение чисел Фибоначчи рекурсивным методом.

def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)