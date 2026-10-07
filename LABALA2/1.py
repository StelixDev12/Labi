def print_1_to_n(n):
    if n > 1:
        print_1_to_n(n - 1)
    print(n, end=" ")


# Пример вызова:
n = int(input())
print_1_to_n(n)
