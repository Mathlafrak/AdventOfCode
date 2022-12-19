data = open("day08_2021.txt", 'r')
input = data.readlines()
def Organize():
    global focus
    focus = []
    for lines in input:
        current_list = lines.split('|')
        get = current_list[1]
        get = get.replace('\n', '')
        strings = get.split()
        focus.append(strings)

Organize()
print(focus)
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
            else:
                checkOtherCase(word)

checkEasyCase()

print(compteur)


def checkOtherCase(word):
    if len(word) == 5:
        print("2,3 et 5 sont possibles")
    if len(word) == 6:
        print("0,6 et 9 sont possibles")
