with open("input.txt") as f:
    items = f.read()

res = []
summa = 0
for i in items.split('\n'):
    if i != '':
        summa += int(i)
    if i == '':
        res.append(summa)
        summa = 0

res = list(reversed(sorted(res)))
print(sum(res[0:3]))