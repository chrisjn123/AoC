#with open('test.txt', 'r') as fh:
with open('input.txt', 'r') as fh:
    lines = fh.readlines()
    L = [line.split()[0] for line in lines]
    R = [line.split()[1] for line in lines]

guide = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors" 
}
beats = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

scoreA = 0

for l, r in zip(L, R):
    opp = guide[l]
    if r == "X":
        me = beats[guide[l]]
    elif r == 'Y':
        me = opp
    else:
        if opp == 'Scissors':
            me = "Rock"
        elif opp == 'Rock':
            me = 'Paper'
        else:
            me = "Scissors"

    scoreA += score[me]
    if opp == me:
        scoreA += 3
    elif opp == "Rock" and me == "Paper":
        scoreA += 6
    elif opp == "Paper" and me == "Scissors":
        scoreA += 6
    elif opp == "Scissors" and me == "Rock":
        scoreA += 6
    else:
        pass
    #print(f'\t{scoreA}')
print(scoreA)