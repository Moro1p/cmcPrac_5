while num := input():
    if int(num) == 13:
        break
    if not int(num) % 2:
        print(num)
else:
    print("13 not found. Congratulations!")
