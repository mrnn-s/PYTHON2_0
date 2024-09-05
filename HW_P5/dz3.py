#Создайте функцию генератор чисел Фибоначчи

n = int(input("N = "))
some_list = []

def fibbPositive(n):
    if n == 1 or n == 2:
        return 1
    return fibbPositive(n - 1) + fibbPositive(n - 2)

for i in range(1, n + 1):                   # формируем список чисел фибоначчи
    some_list.append(fibbPositive(i))
print(some_list)

def fib(n: int):
    x1, x2 = 1, 1
    for i in range(n):
        if i == 0:
            yield x1
        elif i == 1:
            yield x2
        else:
            x1, x2 = x2, x1 + x2
            yield x2

n = int(input('Номер числа фибоначчи ->>> '))
print(*fib(n))
