"""
Реализовать сложение, вычитание и
умножение матриц.
"""
r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

print("Введите первую матрицу:")
A = []
for i in range(r):
    # генератор списка: split() даёт список строк, int(x) превращает каждую в число
    c = [int(x) for x in input().split()]
    A.append(c)

print("Введите вторую матрицу:")
B = []
for i in range(r):
    c = [int(x) for x in input().split()]
    B.append(c)

# Функция сложения (поэлементно)
def add(m1, m2):
    res = []
    for i in range(len(m1)):
        c = []
        # len(m1[0]) — число столбцов (длина первой строки)
        for j in range(len(m1[0])):
            c.append(m1[i][j] + m2[i][j])
        res.append(c)
    return res

# Функция вычитания (поэлементно)
def sub(m1, m2):
    res = []
    for i in range(len(m1)):
        c = []
        for j in range(len(m1[0])):
            c.append(m1[i][j] - m2[i][j])
        res.append(c)
    return res

# Функция умножения (строка на столбец)
def mul(m1, m2):
    res = []
# по строкам первой
    for i in range(len(m1)):          
        c = []
        for j in range(len(m2[0])):   # j — столбец результата
            s = 0
            # k — общий индекс: столбцы m1 и строки m2
            # условие умножения: len(m1[0]) == len(m2), иначе IndexError
            for k in range(len(m2)):
                s += m1[i][k] * m2[k][j]
            c.append(s)
        res.append(c)
    return res


print(f"\nСложение: {add(A, B)}")
print(f"Вычитание: {sub(A, B)}")
print(f"Умножение: {mul(A, B)}")