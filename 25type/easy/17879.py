def dell(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(800000,801000):
    d = dell(x)
    if len(d) != 0:
        m = min(d) + max(d)
        if m%10 == 4:
             print(x,m)