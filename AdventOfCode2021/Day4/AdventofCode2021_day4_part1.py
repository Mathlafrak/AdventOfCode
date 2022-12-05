import numpy as np
import array
data = open("day04.in", 'r')

def numberListMaking():
    numbers = []
    for line in data:
        ligne_intermediaire = line.split()
        numbers.append(ligne_intermediaire)

    string_called_numbers = numbers[0]
    string_called_numbers = string_called_numbers[0].split(",")

    called_numbers = []
    for i in range(len(string_called_numbers)):
        called_numbers.append(int(string_called_numbers[i]))
    j = 0
    bingoSlice = []
    bingoList = []
    for elements in called_numbers:
        if len(bingoSlice) < 5:
            bingoSlice.append(elements)
            if len(bingoList) == 19:
                bingoList.append(bingoSlice)
        else :
            bingoList.append(bingoSlice)
            bingoSlice = []
            bingoSlice.append(elements)
    print(bingoList)
    del numbers[0]
    for lines in numbers:
        if len(lines) == 0:
            numbers.remove(lines)


numberListMaking()

def boardMaking():
    billBoards = []
    board =[]
    i = 0
    K = 0
    for element in numbers:

        intNumbers = []
        for i in range(len(element)):
            intNumbers.append(int(element[i]))

        if len(board) < 5:
            board.append(intNumbers)
            if len(billBoards) == 99 and len(board) == 5:
                billBoards.append(board)
        else:
            billBoards.append(board)
            board = []
            board.append(intNumbers)

            
boardMaking()            
    #print(billBoards)
#  bill_boards [0]     [1]   [0]
#            [index]   [y]   [x]



arrayMatrixIndicator =np.zeros((100, 5, 5))
matrixIndicator = arrayMatrixIndicator.tolist()
matrice = 0
ligne = 0
# def IndexCheck():



def indexColumn(matrice, element):
    if matrixIndicator[matrice][0][element] + matrixIndicator[matrice][1][element] + matrixIndicator[matrice][2][element] +matrixIndicator[matrice][3][element] + matrixIndicator[matrice][4][element] == 5:
        return True
def Checking():
    global winningMatrix
    winningMatrix = []
    global indexWinningMatrix
    indexWinningMatrix = []
    global lastNumber

    for slices in range(len(bingoList)):
    # print(matrixIndicator)
    # print("ok")
    # print(slices)
        for numbers in range(len(bingoList[0])):
            print(numbers)
            a = bingoList[slices][numbers]
            #print(a)
            for matrix in range(len(billBoards)):

                for lign in range(len(billBoards[0])):


                    #print(lign)
                    for element in range(len(billBoards[0][0])):
                        # #print(element)
                        # print(f'numero appelle {bingoList[slices][numbers]}')
                        # print(f' numero de la board {billBoards[matrix][lign][element]}')

                        lastNumber = billBoards[matrix][lign][element]

                        if a == lastNumber:
                            matrixIndicator[matrix][lign][element] += 1
                            # print(f' le numero {newNumber} est dans la matrice {matrix}')
                            # Sum = sum(matrixIndicator[matrix][lign])
                        if sum(matrixIndicator[matrix][lign]) == 5 or indexColumn(matrix, element):
                            winningMatrix = billBoards[matrix]
                            indexWinningMatrix = matrixIndicator[matrix]
                            print(f'la matrice d indice {matrix} est gagnante')

                            return


Checking()
def indexNotCalledNumbers():
    global notCalled
    notCalled = []
    for ligne in range(len(indexWinningMatrix[0])):
        for index in range(len(indexWinningMatrix[0])):
            if indexWinningMatrix[ligne][index] == 0:
                notCalled.append((ligne, index))
    return notCalled

def getNotCalledNumbers(index):
    global somme
    somme = 0
    result = 0
    for element in index:
        y = element[0]
        x = element[1]
        somme += winningMatrix[y][x]
    result = somme*lastNumber
    print(result)





#print(f'{billBoards[84]}')
print(winningMatrix)
print(indexWinningMatrix)

indexNotCalledNumbers()
getNotCalledNumbers(indexNotCalledNumbers())
