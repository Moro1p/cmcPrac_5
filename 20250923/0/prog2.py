sp_digits = [i for i in range(5, 16)]
sp_letters = list("abcdefghijk")
sp_digits[3:7] = sp_letters[-5:]
print(sp_digits)
