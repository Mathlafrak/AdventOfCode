data = open("day08_2022.txt", 'r')
field = []
mapping = []
global compteur
compteur = 0
# field.append(data.readline())
# print(type(field[0]))
# print(len(field[0]))
for lines in data:
    line = []
    lines = lines.replace("\n", "")
    for character in lines:
        character = int(character)
        line.append(character)
    field.append(line)

print(field)
def CheckUp(tree,lines,column):
    UpColumn = []
    for line in field[:lines]:
        UpColumn.append(line[column])
    for element in UpColumn:
        if tree <= element:
            return
        else:
            compteur += 1

def CheckDown(tree, lines, column):
    DownColumn = []
    for line in field[lines:]:
        DownColumn.append(line[column])
    for element in DownColumn:
        if tree <= element:
            return
        else:
            compteur += 1

def CheckRight(tree, lines, column):
    for element in range(len(lines[column:])):
        if tree <= lines[element]:
            return
        else:
            compteur += 1

def CheckLeft(tree, lines, column):
    for element in range(len(lines[:column])):
        if tree <= lines[element]:
            return
        else:
            compteur += 1

def Check(tree,lines,column):
    CheckUp(tree,lines,column)
    CheckDown(tree, lines, column)
    CheckRight(tree, lines, column)
    CheckLeft(tree, lines, column)


for lines in range(len(field)):
    for index in range(len(field[lines])):
        tree = field[lines][index]
        Check(tree, lines, index)

print(compteur)




