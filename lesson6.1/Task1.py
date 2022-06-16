# Создайте программу для игры в "Крестики-нолики".

from operator import truediv
import random
PlayMatrix = list(range(1,10))

def MatrixPrint(Matrix):
   for i in range(3):
      print( Matrix[0+i*3], Matrix[1+i*3], Matrix[2+i*3])

def Player (Matrix):
    YourNumber = int(input('Выберите номер ячейки:'))
    if Matrix[YourNumber-1] == 'X':
        print ('Ячейка занята')
    elif Matrix[YourNumber-1]=='0':
        print ('Ячейка занята')
    elif YourNumber >0 and YourNumber<10:
        Matrix[YourNumber-1] = 0
    else:
        print ('Неверный номер ячейки')
    return Matrix

def Comp (Matrix):
    CompNumber = random.randint(0,8) 
    if Matrix[CompNumber] != '0' or Matrix[CompNumber] !='X':
        Matrix[CompNumber] = 'X'
    else:
        NewCount = 0
        while NewCount <9:
            if Matrix[NewCount]!= '0' or Matrix[NewCount] !='X':
                Matrix[CompNumber] = Matrix[NewCount]
                break
            else:
                NewCount = NewCount+1
    print ('Выбор компьютера: ')
    return Matrix

def Win (Matrix):
    if Matrix[0] == Matrix[4] == Matrix[8]:
        return True
    elif Matrix[2] == Matrix[4] == Matrix[6]:
        return True
    elif Matrix[0] == Matrix[1] == Matrix[2]: 
        return True
    elif Matrix[3] == Matrix[4] == Matrix[5]:
        return True
    elif Matrix[6] == Matrix[7] == Matrix[8]:
        return True
    elif Matrix[0] == Matrix[3] == Matrix[6]:
        return True
    elif Matrix[1] == Matrix[4] == Matrix[7]:
        return True
    elif Matrix[2] == Matrix[5] == Matrix[8]:
        return True
    else:
        return False

def Control (Matrix):
    for i in range(0,8):
        if Matrix[i] != '0' or Matrix[i] != 'X':
            return True
        else:
            return False

MatrixPrint(PlayMatrix)

while Control(PlayMatrix) == True:
    Player(PlayMatrix)
    MatrixPrint(PlayMatrix)
    if Win(PlayMatrix) == True:
        print('Вы выиграли!')
        break
    Comp(PlayMatrix)
    MatrixPrint(PlayMatrix)
    if Win(PlayMatrix) == True:
        print('Выиграл компьютер!')
        break

