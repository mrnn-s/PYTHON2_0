#3.Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным.
# Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

UPPER_LIMIT = 100000
LOW_LIMIT = 0
ONE = 1
ZERO = 0
#
num = int(input(f'Введите число от {LOW_LIMIT} до {UPPER_LIMIT}: '))
if num < LOW_LIMIT or num > UPPER_LIMIT:
     result = 'Действует ограничение на ввод отрицательных чисел и чисел больше 100 000!'
elif num == ONE or num == LOW_LIMIT:
     result = f'число {num} - ни простое ни составное'
elif num % 2 != ZERO:
     result = f'число {num} - составное'
else:
    result = f'число {num} - простое'
print(result)

num = -1
while num < 0 or num > 100000:
     num = int(input(f'Введите число от 0 до 100000: '))
if num == 1 or num == 0:
     result = f'число {num} - ни простое ни составное'
elif num % 2 != 0:
     result = f'число {num} - составное'
else:
     result = f'число {num} - простое'
print(result)

