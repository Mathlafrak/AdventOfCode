
import math
data = open("day07_2021.txt", 'r')
data = data.readline().split(",")

def Convert():
    for element in range(len(data)):
        data[element] = int(data[element])
    print(data)
Convert()

def GetResult():
    a = len(data)
    Index = [0] * a
    for element in range(len(data)):

        for numbers in range(len(data)):

            distance = abs(element - data[numbers])
            Somme = (distance + 1)*distance/2
            Index[element] += Somme
    indice = Index.index(min(Index))
    print(min(Index))
GetResult()