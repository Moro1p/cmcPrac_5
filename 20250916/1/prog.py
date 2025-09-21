num = int(input())
if num % 2 == 0 and num % 25 == 0:
    print("A +", end=" ")
else:
    print("A -", end=" ")
if num % 2 and num % 25 == 0:
    print("B +", end=" ")
else:
    print("B -", end=" ")
if num % 8 == 0:
    print("C +")
else:
    print("C -")
