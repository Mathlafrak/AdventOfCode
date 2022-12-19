annexes = open("day02.txt", "r")
#annexe = annexes.readlines()

mouvementX = 0
aim = 0
depth = 0

for mouvements in annexes:
    if "forward" in mouvements:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                mouvementX = mouvementX + int_char
                depth = depth + aim * int_char

    elif "up" in mouvements:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                aim = aim - int_char


    else:
        for character in mouvements:
            if character.isdigit():
                int_char = int(character)
                aim = aim + int_char








print("Depth = ", depth)

print("Horizontal Position = ", mouvementX)
result = depth*mouvementX
print("Result is : ", result)
