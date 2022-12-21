import numpy as np

data = open("day05_2021.txt", 'r')

movesList = []
begining = []
GenralList = []
for moves in data:
    moves = moves.split()
    del moves[1]
    # print(moves)
    for XY in moves:
        coordonates = XY.split(",")
        x = int(coordonates[0])
        y = int(coordonates[1])
        board = (x, y)
        if len(movesList) < 2:
            movesList.append(board)
            if len(GenralList) == len(moves) - 1:

                GenralList.append(movesList)
        else:
            GenralList.append(movesList)
            movesList = []
            movesList.append(board)

        x = []
        y = []
# print(GenralList)
VentShower = np.zeros((1000,1000))
VentsShower = VentShower.tolist()
# print(len(GenralList))
def DiagonaleMoves(x1,y1,x2,y2):

    if x1 > x2 and y1 > y2: #Descente à gauche

        for i in range(abs(y1 - y2) + 1):

            if (y1 - i >= y2):
                VentsShower[y1 - i][x1 - i] += 1

    if x1 < x2 and y1 > y2: #Descente à droite

        for i in range(abs(y1 - y2) + 1):

            if (y1 - i >= y2):
                VentsShower[y1 - i][x1 + i] += 1

    if x1 > x2 and y1 < y2:
        for i in range(abs(x1 - x2) + 1):

            if (y1 + i <= y2):
                VentsShower[y1 + i][x1 - i] += 1
    if x1 < x2 and y1 < y2:
        for i in range(abs(x1 - x2) + 1):

            if (y1 + i <= y2):
                VentsShower[y1 + i][x1 + i] += 1










def Removings():

    for vents in range(len(GenralList)):
        x1 = GenralList[vents][0][0]
        y1 = GenralList[vents][0][1]
        x2 = GenralList[vents][1][0]
        y2 = GenralList[vents][1][1]

        if x1 == x2:

            for i in range(abs(y1 - y2)+1):
                if y1 <= y2:

                    VentsShower[y1 + i][x1] +=1



                if y2 <= y1:
                    VentsShower[y2 + i][x1] +=1


        elif y1 == y2:

            for i in range(abs(x1 - x2)+1):
                if x1 <= x2:

                    VentsShower[y2][x1 + i] += 1



                if x2 <= x1:

                    VentsShower[y2][x2 + i] +=1

        else :
            DiagonaleMoves(x1, y1,x2, y2)






Removings()
def Marking():
    global compteur
    compteur = 0
    for lignes in range(len(VentsShower)):
        for colonnes in range(len(VentsShower[lignes])):
            if VentsShower[lignes][colonnes] > 1:

                compteur += 1

# print(VentsShower)
Marking()
print(compteur)


