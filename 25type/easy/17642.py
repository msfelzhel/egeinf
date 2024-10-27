def dell(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(800000,800008):
    d = dell(x)
    k = set()
    for j in d:
        if j%10 == 9 and j != 9:
            k.add(j)
    k = sorted(k)
    if len(k) != 0:
        print(x,min(k))
