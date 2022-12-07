data = open("day02_2022.txt", 'r')

def Opening():
    global liste
    liste = []
    for moves in data:
        moves = moves.split()
        liste.append(moves)
    return liste

def ScoreDefining(list):
    global score
    global win
    global loose
    global draw
    global rock
    global paper
    global scissors
    global situation

    rock = 1
    paper = 2
    scissors = 3
    score = 0
    win = 6
    loose = 0
    draw = 3
    situation = [("A", paper, rock, scissors), ("B", scissors, paper, rock), ("C", rock, scissors, paper)]
    for element in list:
        if element[0] == 'A':
            if element[1] == 'X':
                score += scissors + loose
            if element[1] == 'Y':
                score += rock + draw
            if element[1] == 'Z':
                score += paper + win
        if element[0] == 'B':
            if element[1] == 'X':
                score += rock + loose
            if element[1] == 'Y':
                score += paper + draw
            if element[1] == 'Z':
                score += scissors + win

        if element[0] == 'C':
            if element[1] == 'X':
                score += paper + loose
            if element[1] == 'Y':
                score += scissors + draw
            if element[1] == 'Z':
                score += rock + win
    print(score)

ScoreDefining(Opening())