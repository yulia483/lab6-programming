"""
Реализовать алгоритм quicksort
"""

def quick_sort(a):
    # Базовый случай
    if len(a) <= 1:
        return a
    # Выбираем опорный элемент (центральный)
    p = a[len(a) // 2]
    # Делим на три списка: меньше, равно, больше
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    r = [x for x in a if x > p]
    # Рекурсивно сортируем и склеиваем
    return quick_sort(l) + m + quick_sort(r)
# Ввод чисел через пробел
print("Введите числа через пробел:")
a = [int(x) for x in input().split()]
print(f"Исходный: {a}")
print(f"Отсортированный: {quick_sort(a)}")