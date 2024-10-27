def dell(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(18782,18822+1):
    d = dell(x)
    k = set()    
    for j in d:
        if j%2 != 0:
            k.add(j)
    k = sorted(k)
    if len(k) == 3: 
        print(k[0],k[1],k[2])