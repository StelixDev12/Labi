def print_range(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        print_range(a + 1, b)
    else:
        print_range(a - 1, b)


# Пример вызова:
a = int(input())
b = int(input())
print_range(a, b)
