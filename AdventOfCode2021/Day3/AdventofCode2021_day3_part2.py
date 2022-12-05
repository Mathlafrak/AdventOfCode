annexe = open("day03.txt", "r")

data = [x for x in annexe.read().split("\n")]
print(data)
gama_bit = [0]*12
for element in data:
    i = 0
    for character in element:
        if character == "1":
            gama_bit[i] += 1
        i += 1

print(gama_bit)
gama_rate = [0]*12
j = 0
for mesures in gama_bit:
    if mesures > 500:
        gama_rate[j] = "1"
    j += 1

print(gama_rate)

second_data = data.copy()
position = 0
while len(data) >1:
    un = 0
    zero = 0
    uns = []
    zeros = []
    for element in range(0, len(data)):
        if data[element][position] == "0":
            zero += 1
            zeros.append(data[element])
        else:
            un += 1
            uns.append(data[element])
    if zero > un:
        data = zeros
    else :
        data = uns
    position += 1
oxygen_bit = int(data[0], 2)
print(oxygen_bit)

position = 0
data = second_data
while len(data) >1:
    un = 0
    zero = 0
    uns = []
    zeros = []
    for element in range(0, len(data)):
        if data[element][position] == "0":
            zero += 1
            zeros.append(data[element])
        else :
            un += 1
            uns.append(data[element])
    if zero > un:
        data = uns
    else:
        data = zeros
    position += 1

co2_bit = int(data[0], 2)
print(co2_bit)

print("Result is : ", oxygen_bit*co2_bit)





