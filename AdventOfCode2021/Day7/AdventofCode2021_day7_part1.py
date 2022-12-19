data = open("day07_2021.txt", 'r')
data = data.readline().split(",")
print(data)
for element in range(len(data)):
    data[element] = int(data[element])


def GetMinimum():
    global indice
    a = len(data) #1940
    L = [0] * a

    for element in range(len(data)):
        for numbers in range(len(data)):
            L[element] += abs(element - data[numbers])

    indice = L.index(min(L))

GetMinimum()
def GetResult():
    fuel = 0
    for element in data:
        fuel += abs(element - indice)
    print(fuel)

GetResult()
