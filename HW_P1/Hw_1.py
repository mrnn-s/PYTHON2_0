# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input('Сторона треугольника a: '))
b = float(input('Сторона треугольника b: '))
c = float(input('Сторона треугольника c: '))
triangle1 = a == b and b == c
triangle2 = a == b or b == c or a == c
triangle3 = a != b and b != c and a != c
if triangle1:
     print('Ваш треугольник равносторонний')
elif triangle2:
     print('Ваш треугольник равнобедренный')
elif triangle3:
     print('Ваш треугольник разносторонний')
else:
     print("Треугольника с такими сторонами не существует")
