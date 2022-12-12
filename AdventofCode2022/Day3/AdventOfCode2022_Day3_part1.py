import string
data = open("day03_2022.txt", 'r')
input = []
for lines in data:
    lines = lines.replace('\n', '')
    input.append(lines)

print(len(input))

def SplitWord(string):
    global finding
    finding = []
    global bag
    cut = int(len(string)/2)

    finding.append(set(string[:cut]))
    finding.append(set(string[cut:]))

    return finding

    # print(finding)
compteur = 0
def GetPriority(list):
    global compteur
    global priority
    letter = []
    priority = list[0].intersection(list[1])
    priority = " ".join(priority)


    if priority in ALPHABET:
        compteur += 27 + ALPHABET.index(priority)
    else:
        compteur += alphabet.index(priority) + 1


alphabet = string.ascii_lowercase
ALPHABET = string.ascii_uppercase
# print(alphabet)
# print(ALPHABET)

for element in range(len(input)):
    GetPriority(SplitWord(input[element]))
print(compteur)

