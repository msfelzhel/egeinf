k = 0
for x in range(2**15):
    b = bin(x)[2:]
    if (3+3+b.count('1'))%11 == 0:
        k+=1
print(k)
