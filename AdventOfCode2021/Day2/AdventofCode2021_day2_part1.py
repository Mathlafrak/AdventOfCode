annexes = open("day02.txt", "r")

mouvementX = 0
mouvementUp = 0
mouvementDown = 0

for mouvements in annexes:
    if "forward" in mouvements:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                mouvementX = mouvementX + int_char

    if "up" in mouvements:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                mouvementUp = mouvementUp + int_char


    if "down" in mouvements:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                mouvementDown = mouvementDown + int_char





print(mouvementUp)
print(mouvementDown)

mouvementY = mouvementDown - mouvementUp
print("Depth = ", mouvementY)

print("Horizontal Position = ", mouvementX)
result = mouvementY*mouvementX
print("Result is : ", result)
