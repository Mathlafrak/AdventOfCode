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
        gama_rate[j] += 1
    j += 1

print(gama_rate)


