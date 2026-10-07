def prime_factors(n, d=2):
    if n <= 1:
        return
    if n % d == 0:
        print(d, end=" ")
        prime_factors(n // d, d)
    else:
        prime_factors(n, d + 1)


# Пример вызова:
n = int(input())
prime_factors(n)
