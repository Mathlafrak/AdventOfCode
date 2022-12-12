
import math
data = open("day07_2021.txt", 'r')
data = data.readline().split(",")
print(data)
for element in range(len(data)):
    data[element] = int(data[element])


a = max(data) #1940
L = [0]*a
print(L)
fuelListe = []
liste = []
for indice in range(len(L)):
    for element in range(len(data)):
        fuel = 0
        i = 0

        if data[element] > indice:
            while data[element] - i != indice:
                fuel += i
                i += 1
        if data[element] < indice:
            while data[element] + i != indice:
                fuel += i
                i += 1
        fuelListe.append(fuel)

print(min(fuel))
print(L.index(min(L)))



print(fuel)


