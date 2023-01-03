data = open("day05_2022.txt",'r')
Stack1 = ['Q','S','W','C','Z','V','F','T']
Stack2 = ['Q','R','B']
Stack3 = ['B','Z','T','Q','P','M','S']
Stack4 = ['D','V','F','R','Q','H']
Stack5 = ['J','G','L','D','B','S','T','P']
Stack6 = ['W','R','T','Z']
Stack7 = ['H','Q','M','N','S','F','R','J']
Stack8 = ['R','N','F','H','W']
Stack9 = ['J','Z','T','Q','P','R','B']
InitialState = [Stack1,Stack2,Stack3,Stack4,Stack5,Stack6,Stack7,Stack8,Stack9]

input = []
for lines in data:
    lines = lines.split()
    input.append(lines)
del input[0:10]

print(input)
for lines in input:
    quantity = int(lines[1])
    sender = int(lines[3])
    receiver = int(lines[5])
    for i in range(quantity):
        InitialState[receiver - 1].append(InitialState[sender - 1].pop())

Result = [Stack1[len(Stack1)-1],Stack2[len(Stack2)-1],Stack3[len(Stack3)-1],Stack4[len(Stack4)-1],Stack5[len(Stack5)-1],Stack6[len(Stack6)-1],Stack7[len(Stack7)-1],Stack8[len(Stack8)-1],Stack9[len(Stack9)-1]]
print(Result)





