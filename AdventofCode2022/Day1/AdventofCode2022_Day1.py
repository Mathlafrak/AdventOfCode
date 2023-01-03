data = open("/home/g700830/Workspace/AdventofCode/AdventofCode2022/Day1/day01_2022.in", "r")

datas = data.read().split("\n\n")
print(datas)
string_elvesList = []
for elements in datas:
    interm = []
    interm = elements.split("\n")
    string_elvesList.append(interm)
print(string_elvesList)
print(len(string_elvesList))
elvesCarry = []
for elements in range(len(string_elvesList)):
    carry = []
    for numbers in string_elvesList[elements]:
        nombre = int(numbers)
        carry.append(nombre)
    elvesCarry.append(carry)
print(elvesCarry)
print(len(elvesCarry))
Sums = []
for elves in range(len(elvesCarry)):
    Sums.append(sum(elvesCarry[elves]))

print(Sums)
firstMax = max(Sums)
print(firstMax)
Sums.remove(max(Sums))
secondMax = max(Sums)
print(max(Sums))
Sums.remove(max(Sums))
thirdMax = max(Sums)
print(thirdMax)

result = firstMax + secondMax + thirdMax
print(result)

#print(elvesList)
