data = open("day07_2022.txt",'r')
input = []
compteur = 0
for lines in data:
    lines = lines.split()
    input.append(lines)
    # print(lines)

currentDirectory = []
for lines in range(len(input)):
    input[lines] = input[lines].split()
    if input[lines][0] == '$':
        if input[lines][1] == 'cd':

            if input[lines][2] == '..':

        if input[lines][1] == 'ls':




print(compteur)
