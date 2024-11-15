k = 0
for x in range(2**20):
    b = bin(x)[2:]
    if (5+b.count('1'))%5 == 0:
        k+=1
print(k)
