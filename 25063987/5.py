for n in range(1,1000):
    nn = bin(n)[2:]
    if n%5 == 0:
        nn = nn[0:3:] + nn 
    else: 
        nn = nn + bin(5*(n%5))[2:]
    r = int(nn,2)
    if r < 313 and n&2 != 0:
        print(n)
