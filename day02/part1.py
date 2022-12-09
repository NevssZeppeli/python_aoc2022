with open('input.txt', 'r') as f:
    items = f.read()

# Rock:     A X
# Paper:    B Y
# Scissors: C Z

win  = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
lose = ['A Z', 'B X', 'C Y']

scores = []

for x in items.split('\n'):
    score = 0
    if 'X' in x:
        score += 1
    if 'Y' in x:
        score += 2
    if 'Z' in x:
        score += 3

    if x in lose:
        pass
    if x in draw:
        score += 3
    if x in win:
        score += 6
    scores.append(score)

print(sum(scores))