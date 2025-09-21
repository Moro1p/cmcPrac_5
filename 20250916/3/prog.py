n = int(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        mul = (n + i) * (n + j)
        sum_digits = 0
        while mul:
            sum_digits += mul % 10
            mul //= 10
        if sum_digits == 6:
            print(n + i, "*", n + j, "=", ":=)", sep=" ", end=" ")
        else:
            print(n + i, "*", n + j, "=", (n + i) * (n + j), sep=" ", end=" ")
        j += 1
    i += 1
    print()
