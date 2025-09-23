sp = []
while s := input():
    sp.append([int(x) for x in s.split()])

if all(len(x) == len(sp[0]) for x in sp):
    for i in range(len(sp)):
        for j in range(len(sp[i])):
            print(sp[j][i], end=" ")
        print()
else:
    print("Invalid matrix")
