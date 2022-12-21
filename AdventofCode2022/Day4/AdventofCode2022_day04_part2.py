import re
data = open("/home/g700830/Workspace/AdventofCode/AdventofCode2022/Day4/day04_2022.txt",'r')

input = []
for lines in data:

    lines = lines.replace("\n", "")

    Split = re.split(r'-|,', lines)
    input.append(Split)

transit = []
for lines in input:   
    moove = []
    for character in lines:
        if character.isdigit():
            moove.append(int(character))    
    transit.append(moove)
compteur = 0 

for mooves in transit:
    a = mooves[0]
    b = mooves[1]
    c = mooves[2]
    d = mooves[3]
    if a >= c and b <= d:
        compteur += 1
    elif a <= c and b >= d:
        compteur += 1
    elif a <= c and b >= c:
        compteur += 1
    elif a >= c and a <= d:
        compteur += 1
    else:
        compteur = compteur 




print(compteur)
