annexe = open("/home/g700830/Workspace/AdventofCode/AdventOfCode2021/Day3/day03.txt", "r")

data = [x for x in annexe.read().split("\n")]

gama_bit = [0]*12
for element in data:
    i = 0
    for character in element:
        if character == "1": # if character == Si egale à 1 == True/0 == False
            gama_bit[i] += 1
        i += 1

gama_rate = [0]*12
j = 0
for mesures in gama_bit:
    if mesures > len(data)/2:
        gama_rate[j] += 1
    j += 1

print(gama_rate)
epsilon_rate = gama_rate.copy()
def GetEpsilonRate(epsilonrate):
    for element in range(len(epsilonrate)):
        if epsilonrate[element] == 1:
            epsilonrate[element] = 0
        else:
            epsilonrate[element] = 1
    return epsilonrate

print(GetEpsilonRate(epsilon_rate))

def GetPower2(rate):
    for bits in range(len(rate)):
        rate[bits] = rate[bits]*pow(2,len(rate)-bits -1)
    return rate
print(GetPower2(gama_rate))
print(GetPower2(epsilon_rate))
print(sum(GetPower2(gama_rate)))
Result_Gama = sum(GetPower2(gama_rate))
Result_Epsilon = sum(GetPower2(epsilon_rate))
print(f' Result is Result_Gama * Result_Epsilon = {Result_Gama}*{Result_Epsilon} = ', Result_Gama*Result_Epsilon)


