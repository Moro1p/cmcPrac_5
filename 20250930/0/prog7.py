def create_adders():
    adders = []
    for i in range(10):
        def adder(x, y=i):
            return y + x
        adders.append(adder)
    return adders

for adder in create_adders():
    print(adder(1))
