k = 0
for x in range(2**11):
    b = bin(x)[2:]
    if (b.count('1') + 8)%5 != 0:
        k+=1
print(k)
