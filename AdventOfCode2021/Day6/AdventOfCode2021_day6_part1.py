data = open("day06_2021.in", 'r')
input = data.readline()
lanternList = input.split(",")
lanterFishList = []
for fish in lanternList:
    fish = int(fish)
    lanterFishList.append(fish)

print(lanterFishList)
TimeCompteur = [0,0,0,0,0,0,0,0,0]
def TimeCounting(list):


    for x in range(8):
        for fish in lanterFishList:
            if fish == x:
                list[x] += 1
    return list


def Calculating(list):

    for days in range (256):
        next = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        print("GO")
        print(list)

        for indice in range(len(list)):

            next[indice-1] = list[indice]
        next[6] += list[0]
        list = next.copy()
        print(list)
        print("\n")


            # print(indice)

    return list

# print(TimeCompteur)
TimeCompteur = Calculating(TimeCounting(TimeCompteur))
# print(TimeCompteur)
result = 0

for count in TimeCompteur:
    result += count
print(result)








