sp = []
while s := input():
    sp.append([int(x) for x in s.split()])

for i in range(len(sp)):
    for j in range(i + 1, len(sp[i])):
        sp[i][j], sp[j][i] = sp[j][i], sp[i][j]
for elem in sp:
    print(elem)
