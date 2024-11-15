k = 0
for x in range(2**13):
    b = bin(x)[2:]
    if (b.count('1') + 14)%6 != 0 and b[-4:] == '1000':
        k+=1
print(k)
