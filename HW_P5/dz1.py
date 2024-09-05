# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

path = r"c:\temp\text.txt"

def truePath(path):
     tempIndex = path.rfind('.')
     extension = path[tempIndex+1:len(path)]
     endIndex = tempIndex
     tempIndex = path.rfind('\\')
     nameOfFile = path[tempIndex+1:endIndex]
     pathToFile = path[0:tempIndex+1]
     return (pathToFile, nameOfFile, extension)

print(truePath(path))
path = truePath(path)
print(path[0])