import string
data = open("/home/g700830/Workspace/AdventofCode/AdventofCode2022/Day3/day03_2022.txt", 'r')
input = []
group = []
for lines in data:
    lines = lines.replace('\n', '')
    if len(group) < 3:
        group.append(lines)
        if len(input) == 99:
            input.append(group)
    else:
        input.append(group)
        group = []
        group.append(lines)

print(input)
input = [set(s) for s in input]
print(input)
def GetPriority(liste):
    global commonLetters
    commonLetters = []
    for element in liste:
        common = set.intersection(*map(set,element)) #Get the common character between the 3 strings of the set "element"
        commonLetters.append(list(common))
    
    print(commonLetters)
    return GetValue(commonLetters)

    # return compteur



def GetValue(common_letter):
    global compteur
    compteur = 0
    alphabet = string.ascii_lowercase
    ALPHABET = string.ascii_uppercase
    for letters in range(len(common_letter)):
        if common_letter[letters][0] in ALPHABET:
            compteur += 27 + ALPHABET.index(common_letter[letters][0])
        else:
            compteur += alphabet.index(common_letter[letters][0]) + 1
    return compteur

print(GetPriority(input))


