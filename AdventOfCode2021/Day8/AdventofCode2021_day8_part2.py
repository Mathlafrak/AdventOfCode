import copy

data = open("day08_2021.txt", 'r')
input = data.readlines()
def Organize():
    global focus
    focus = []
    global firstFocus
    firstFocus = []
    for lines in input:
        current_list = lines.split('|')
        get = current_list[1]
        firstGet = current_list[0]
        get = get.replace('\n', '')
        strings = get.split()
        firstStrings = firstGet.split()
        focus.append(strings)
        firstFocus.append(firstStrings)

Organize()
print(firstFocus)
def checkEasyCase():
    global compteur
    compteur = 0
    global digits
    digits = []
    for packs in range(len(focus)):

        for digit in range(4):
            word = focus[packs][digit]
            if len(word) == 2: #Number 1
                compteur += 1
            elif len(word) == 4: #Number 4
                compteur += 1
            elif len(word) == 3: #Number 7
                compteur += 1
            elif len(word) == 7: #Number 8
                compteur += 1
            # else:
                # checkOtherCase(word)


# def checkOtherCase(word):
#     if len(word) == 5:
#         print("2,3 et 5 sont possibles")
#     if len(word) == 6:
#         print("0,6 et 9 sont possibles")


lenEasy = [2, 3, 4, 7]


one = [1,2,['a','b']] # number = [int, len,[l,e,t,t,e,r,s]]
four = [4,4,['a','b','e','f']]
seven = [7,3,['d','a','b']]
eight = [8,7,['a','b','c','d','e','f','g']]
EasyTuples = [one, four, seven, eight]


def GetEasyOnes(line):
    global EasyOnes
    EasyOnes = []
    for element in line:
        if len(element) in lenEasy:
            EasyOnes.append(element)
    return EasyOnes

def IdentifyFromLen(element):
    global number
    for numbers in range(len(EasyTuples)):
        if len(element) == EasyTuples[numbers][1]:
            number = EasyTuples[numbers].copy()
            print("got it ")
            return number
        else:
            print("Unknown number")

def GetLawsFromEasy(Easytable): #Easytable contains the easy digits

    for element in range(len(Easytable)):
        number = IdentifyFromLen(Easytable[element])
        for wrongCharacter in Easytable[element]:

            if wrongCharacter not in number[2]:
                GetRightCharacter(firstFocus[0], wrongCharacter)

def GetCharactersOfNumber(number): #Get the model list of characters of the number
    CharacterList = number[2]
    return CharacterList    

def GetRightCharacter(string, character):
    global lawTuple
    global Laws
    Laws = []
    for chars in range(len(number[2])):
        if character != number[2][chars] and character not in number[2]:
            lawTuple = (character, number[2][chars])
            Laws.append(lawTuple)
            string[chars].replace(character, number[2][chars])
            print(character)
    return Laws
            

GetLawsFromEasy(firstFocus)