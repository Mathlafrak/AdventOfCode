data = open("/home/g700830/Workspace/AdventofCode/AdventofCode2022/Day8/day08_2022.txt", 'r')

print("begin")
def SettingUp():
    global compteur 
    global field
    compteur = 0
    field = []
SettingUp()

for lines in data:
    line = []
    lines = lines.replace("\n", "")
    for character in lines:
        character = int(character)
        line.append(character)
    field.append(line)



def CheckRight(lign, column):
    currentList = field[lign][column:]
    # print(currentList)
    element = field[lign][column]
    maxHeight = max(currentList)
    if element == maxHeight and currentList.count(max(currentList)) == 1:
        return True
    else:
        return False

def CheckLeft(lign, column):
    currentList = field[lign][:column + 1]
    element = field[lign][column]
    maxHeight = max(currentList)
    if element == maxHeight and currentList.count(max(currentList)) == 1:
        return True
    else:
        return False

def CheckUp(lign , column):
    currentList = []
    element = field[lign][column]
    
    for lignes in range(lign + 1):
        currentList.append(field[lignes][column])
    maxHeight = max(currentList)
    if element == maxHeight and currentList.count(max(currentList)) == 1:
        return True
    else:
        return False

def CheckDown(lign, column):
    currentList = []
    element = field[lign][column]
    
    currentLign = len(field[lign]) - lign -1
    for lignes in range(currentLign + 1):
        currentList.append(field[-lignes][column])
    print(element)
    print(currentList)
    maxHeight = max(currentList)
    print(maxHeight)
    if element == maxHeight and currentList.count(max(currentList)) == 1:
        return True
    else:
        return False


def Check(lign, trees):
    global compteur

    if lign == 0 or lign == len(field[lign]) -1 or trees == 0 or trees == len(field[lign])-1:
        compteur = compteur + 1
        print(f' localisation : {lign} + {trees})')
        return
    else:
        if CheckDown(lign, trees):
            compteur = compteur + 1
            print(f' localisation : {lign} + {trees} thanks to CheckDown')
        elif CheckUp(lign, trees):
            compteur = compteur + 1
            print(f' localisation : {lign} + {trees} thanks to CheckUp')
        elif CheckLeft(lign, trees):
            compteur = compteur + 1
            print(f' localisation : {lign} + {trees} thanks to CheckLeft')
        elif CheckRight(lign, trees):
            compteur = compteur + 1
            print(f' localisation : {lign} + {trees} thanks to CheckRight')
        else:
            return 
        

for lines in range(len(field)):
    for trees in range(len(field[lines])):
        Check(lines, trees)  
        
print(compteur)


