sp = [int(x) for x in input().split(',') if x]

for i in range(len(sp)):
    for j in range(i, len(sp)):
        if (sp[i] ** 2) % 100 > (sp[j] ** 2) % 100:
            sp[i], sp[j] = sp[j], sp[i]
print(sp)
