#Задача 1
print("Задача 1")
import random
def selection_sort_asc(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
numbers = [random.randint(2, 103) for _ in range(10)]
print("Исходный массив:")
print(numbers)
sorted_numbers = selection_sort_asc(numbers)
print("Отсортированный по возрастанию:")
print(sorted_numbers)

#Задача 2

print("Задача 2")
import random
def sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
numbers = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:")
print(numbers)
sorted_desc = sort_descending(numbers)
print("Отсортированный по убыванию:")
print(sorted_desc)
#Задача 3
print("Задача 3")
def selection_sort_phones(phones):
    n = len(phones)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if phones[j] < phones[min_idx]:
                min_idx = j
        phones[i], phones[min_idx] = phones[min_idx], phones[i]
    return phones
phone_list = [
    "56-78-12",
    "23-45-67",
    "10-20-30",
    "23-11-99",
    "99-00-11",
    "01-23-45"
]
print("Исходный список номеров:")
print(phone_list)
sorted_phones = selection_sort_phones(phone_list)
print("Отсортированный список по возрастанию:")
print(sorted_phones)