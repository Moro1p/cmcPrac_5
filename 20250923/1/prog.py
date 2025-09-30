m, n = eval(input())
print([x for x in range(m, n) if x != 1 and all([x % i for i in range(2, x)])])
