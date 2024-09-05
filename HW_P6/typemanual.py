from random import randint

n = 8
desk = [[0 for i in range(8)] for j in range(8)]
#координаты в одну строку
#coordinates = 'a1b3c2d5e4f6g7h8'
coordinates = 'h1d2a3c4f5b6g7e8'

#Генерируем координаты ферзя
def rndF():
    alpha = 'abcdefgh'
    i = randint(0,8)
    j = randint(0,8)
    width = alpha[i]
    height = j
    print(width, height)
    return width, height

def addF(i:int, j:int):
    global n
    for k in range(n):
        desk[k][j] += 1
        desk[i][k] += 1
        if 0 <= i + j - k < n: desk[i + j - k][k] += 1
        if 0 <= i - j + k < n: desk[i - j + k][k] += 1
    desk[i][j] = -1
    return desk

#Тут мы смотрим можно ли поставить ферзя или нет
def calculatingF(i:int,j:int):
    bool = True
    k = 0
    if desk[i][j] <= 0:
        addF(i,j)
    else :
        print('Данное размещение ферзей невозможно')
        bool = False
    k +=1
    return bool

#функция для ручной подстановки координат ( они наверху модуля)
def manualF():
    for i in range(0, 16, 2):
        alpha = 'abcdefgh'
        width = coordinates[i]
        height = int(coordinates[i+1])-1
        width =int(alpha.index(width))
        print(f'Проверим ферзя на {coordinates[i]}{coordinates[i+1]}')
        if calculatingF(height, width) == False: break
        else : print('Ok')

def randomF():
    for i in range(0, 16, 2):
        alpha = 'abcdefgh'
        width = randint(1,8)-1
        height = randint(1,8)-1
        width = alpha.index(alpha[width])
        print(f'Проверим ферзя на {alpha[width]}{height+1}')
        if calculatingF(height, width) == False: break
        else : print('Ok')