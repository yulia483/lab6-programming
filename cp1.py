""""
 Реализовать алгоритм сортировки слиянием для списка.
 """
 
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
# Ввод чисел с клавиатуры
print("Введите числа через пробел:")
a = [int(x) for x in input().split()]
print(f"Исходный: {a}")
print(f"Отсортированный: {merge_sort(a)}")