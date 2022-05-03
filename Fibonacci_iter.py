# Определение чисел Фибоначчи итерационным методом.

def fibonacci_iter(n):
    fibonacci_first = 1
    fibonacci_second = 1
    for i in range(2, n):
        fibonacci_n = fibonacci_first + fibonacci_second
        fibonacci_first = fibonacci_second
        fibonacci_second = fibonacci_n
    return fibonacci_n