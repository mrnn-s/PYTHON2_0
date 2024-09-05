#  Данная программа умеет расставлять 8 ферзей на доску 64 клеток, чтобы они друг друга не грызли
#  В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# 
# 
# В конце добавлена функция выбора количества комбинаций для отображения


n = 8 #размер доски, при изменении величины изменить переменную alpha
deskList = []
desk = [[0 for i in range(n)] for j in range(n)]

def setF(i:int,j:int):
    global n
    for k in range(n):
        desk[k][j] += 1
        desk[i][k] += 1
        if 0 <= i+j-k < n: desk[i+j-k][k] +=1
        if 0 <= i-j+k < n: desk[i-j+k][k] +=1
    desk[i][j] =-1

def delF(i:int,j:int):
    global n
    for k in range(n):
        desk[k][j] -=1
        desk[i][k] -=1
        if 0 <=i+j-k < n: desk[i+j-k][k] -=1
        if 0 <=i-j+k < n: desk[i-j+k][k] -=1
    desk[i][j] = 0

def printResult():
    global n
    alpha = 'abcdefgh'
    myList = []
    global deskList
    for i in range(n):
        for j in range(n):
            if desk[i][j] == -1:
                myList.append(alpha[j] + str(i+1))
    print('  '.join(myList))
    deskList.append(myList)
def calcF(i:int):
    for j in range(8):
        if desk[i][j] == 0:
            setF(i,j)
            if i == 7:
                printResult()
            else :
                calcF(i+1)
            delF(i,j)

def printVariants(x:int):
    global n
    myList = []
    for i in range(x):
        myList.append(deskList[i])
        print(" ".join(myList[i]))
calcF(0)
x = int(input('Укажите кол-во вариантов -->> '))
printVariants(x)