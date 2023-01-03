data = open("day06_2022.txt",'r')
Data = data.readline()
input = []
for character in Data:
    input.append(character)
print(input)
def Check(index):
    window = [input[index], input[index +1], input[index +2], input[index +3]]
    if len(window) == len(set(window)):
        print(index + len(window))
        return True
    else:
        return False

def main():
    for element in range(len(input)):
        if Check(element):
            return

main()