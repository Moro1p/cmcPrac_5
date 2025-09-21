summ = 0
while summ < 21:
    num = int(input())
    if num < 0:
        print(num)
        break
    summ += num
else:
    print(summ)
