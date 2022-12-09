with open('input.txt', 'r') as f:
    items = f.read()

# Rock:     A X
# Paper:    B Y
# Scissors: C Z

scores = []

for x in items.split('\n'):
    score = 0
    if 'X' in x:
        if "A" in x:
            score += 3
        if "B" in x:
            score += 1
        if "C" in x:
            score += 2

    if 'Y' in x:
        score += 3 
        if "A" in x:
            score += 1
        if "B" in x:
            score += 2
        if "C" in x:
            score += 3 

    if 'Z' in x:
        score += 6
        if "A" in x:
            score += 2
        if "B" in x:
            score += 3
        if "C" in x:
            score += 1


    scores.append(score)

print(sum(scores))