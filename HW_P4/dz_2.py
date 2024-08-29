#2 задача
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление

def someFunc(**args):
    myDict = {}
    for key, value in args.items():
        #key = value
        if value.__hash__ == None:
            value = str(value)
        myDict[value] = key
    return myDict

print(someFunc(a = 15, b = 'Preved', c = 15.99, d = [2, 3, 4, 5, 6, 7], e = {99, 100, 101}, g = (1, 2, 3, 4, 5)))