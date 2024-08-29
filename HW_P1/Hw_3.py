# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1
while count <= ATTEMPT_COUNT:
     print(f'Попытка {count}. Введите целое число: ')
     num_1 = int(input())
     if num_1 == num:
         print(f'Вы угадали число {num}')
         break
     elif num < num_1:
         print(f'Загаданное число меньше {num_1}')
     else:
         print(f'Загаданное число больше {num_1}')
         count += 1
else:
     print('Попытки закончились, число НЕ угадано,загаданное число {num} ')