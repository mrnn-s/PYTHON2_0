#Напишите функцию для транспонирования матрицы

def matrixTr(myAr):
     for i in range(len(myAr)):
         for j in range(i, len(myAr[i])):
             temp = myAr[i][j]
             myAr[i][j] = myAr[j][i]
             myAr[j][i] = temp
     return myAr
myAr = [[1,2,3,4,5], [6,7,8,9,0], [0,9,8,7,6],[5,4,3,2,1], [3,3,3,3,3]]
for i in myAr:
     print(i)
print()
myAr = matrixTr(myAr)
for i in myAr:
    print(myAr)