def factorial(n):
    print(f'n : {n}.')
    if n == 1:
        return 1
    return n * factorial(n - 1)
f = factorial(3)
print(f)

