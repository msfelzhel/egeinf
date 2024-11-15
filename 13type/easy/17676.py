k = 0
for x in range(2**22):
    b = bin(x)[2:]
    if (7+b.count('1'))%3 != 0:
        k+=1
print(k)
