import string
data = open("day03_2022.txt", 'r')
input = []
group = []
for lines in data:
    if len(group) < 3:
        lines = lines.replace('\n', '')
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
def GetPriority(list):
    global compteur
    global priority
    letter = []

    common = set.intersection(*map(set, list[0]))
   
    print(common)

GetPriority(input)
    # if priority in ALPHABET:
    #     compteur += 27 + ALPHABET.index(priority)
    # else:
    #     compteur += alphabet.index(priority) + 1


# alphabet = string.ascii_lowercase
# ALPHABET = string.ascii_uppercase
# # print(alphabet)
# # print(ALPHABET)
#
# for element in range(len(input)):
#     GetPriority(input[element])
# # print(compteur)

