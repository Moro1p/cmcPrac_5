sp = [int(x) for x in input().split()]
for elem in sp:
    if elem % 2:
        print(elem)
        break
else:
    print(sp[0])
