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



def CheckDown(lign, column):
    direction = DownCheck
    element = field[lign][column]
    
    if LimitCheck(lign + 1,column):
        NextElement = [field[lign + 1][column], lign, column]
        if Compare(element, NextElement, direction):
            CheckDown(lign + 1, column)
        else:
            return False

def CheckUp(lign , column):
    direction = UpCheck 
    element = field[lign][column]
    if LimitCheck(lign -1,column):
        NextElement = [field[lign - 1][column], lign, column]
        
        if Compare(element, NextElement, direction):
            CheckUp(lign - 1, column)
        else:
            return False


def CheckLeft(lign, column):
    direction = LeftCheck
    element = field[lign][column]
    if LimitCheck(lign,column - 1):
        NextElement = [field[lign][column - 1], lign, column]
        if Compare(element, NextElement, direction):
            CheckLeft(lign, column - 1)
        else:
            return False



def CheckRight(lign, column):
    direction = RightCheck
    element = field[lign][column]
    if LimitCheck(lign,column + 1):
        NextElement = [field[lign][column + 1], lign, column]
        if Compare(element, NextElement, direction):
            CheckRight(lign, column + 1)
        else:
            return False



def Compare(element, NextElement, direction):
    if element > NextElement[0]:
        direction += 1
        return True
    elif element <= NextElement[0]: 
        return Stop(direction)
    else:
        return False

def Stop(direction):
    direction = direction + 1
    return direction 

def LimitCheck(lign, column):

    if lign == 0 or lign == len(field) -1 or column == 0 or column == len(field)-1:  # len() -1 car sinon out of range 
        # print(f' localisation : {lign} + {column})')
        return False
    else:
        return True


def Check(lign, column):

    if lign == 0 or lign == len(field[lign]) -1 or column == 0 or column == len(field[lign])-1:  # len() -1 car sinon out of range 
        Result = 0
    else:
        CheckDown(lign, column)

        CheckUp(lign, column)

        CheckLeft(lign, column)

        CheckRight(lign, column)

def Initialize():
    global Result
    global DownCheck
    global UpCheck
    global LeftCheck
    global RightCheck
    DownCheck = 0
    UpCheck = 0
    LeftCheck = 0
    RightCheck = 0

Initialize()        
Results = []
for lines in range(len(field)):
    for column in range(len(field[lines])):
        Check(lines, column)  
        Result = DownCheck * UpCheck * LeftCheck * RightCheck 
        Results.append(Result)
        # print(f' Down : {DownCheck}, Up : {UpCheck}, Left : {LeftCheck}, Right : {RightCheck}')
        print(Result)
        
print(compteur)


