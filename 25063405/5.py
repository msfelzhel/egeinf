g = []
for n in range(10,100):
    nn = bin(n)[2:]
    if n%3 == 0: 
        nn = nn + nn[-2] + nn[-1]
    else:
        nn = nn + bin(3*(n%3))[2:]
    r = int(nn,2)
    if r >= 195:
        g.append(r)
print(min(g))