"""
Найти все дубликаты в списке.
"""

print("введите числа через пробел:")
from collections import Counter

a = [int(x) for x in input().split()]
# Считаем частоту каждого элемента
cnt = Counter(a)
# Оставляем только те, у которых частота > 1
d = [b for b, v in cnt.items() if v > 1]
if d:
    print(f"Дубликаты: {d}")
else:
    print("Дубликатов нет")
