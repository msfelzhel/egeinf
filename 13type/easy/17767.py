k = 0
for x in range(2**12):
    b = bin(x)[2:]
    if (b.count('1') + 11)%5 != 0:
        k+=1
print(k)
